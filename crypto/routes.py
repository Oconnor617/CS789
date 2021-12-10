from werkzeug.utils import redirect
from crypto import app
from crypto.ElGamal import key_gen, encrypt, decrypt, key_gen_root, encrypt_num, decrypt_num
from crypto.Euclidean import *
from crypto.Exponentiation import *
from crypto.Helpers import *
from crypto.PseudoRandoms import *
from flask import render_template, request, flash, url_for
from crypto.PrimRoots import *
import math

from crypto.RSA import rsa_keys, rsa_enc, rsa_dec

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World! - Welcome to my Crypto app for CS789. Let's Go!"
    return render_template('index.html')

@app.route('/gcd', methods=['GET', 'POST'])
def gcd():
    if request.method == 'POST':  # Form Submitted
        GCDM = int(request.form['GCD_M'])
        GCDN = int(request.form['GCD_N'])
        print(GCDM)
        print(GCDN)
        print(type(GCDM))
        print(type(GCDN)) 
        gcd = GCD(GCDM,GCDN)
        print("The GCD of {} and {} is: {}".format(GCDN,GCDM,gcd))
        return redirect(url_for('index'))
    else: 
        return render_template('index') # its a GET request. no form submitted


@app.route('/modInverse', methods=['GET', 'POST'])
def modInverse():
    if request.method == 'POST':
        nummy = int(request.form['num'])
        moddy = int(request.form['mod'])
        print('Num: {} Mod: {}'.format(nummy,moddy))
        g = GCD(nummy,moddy)# find the GCD of the numbers. It will need to be 1 for this to work
        if (g != 1):
            #if we are here it means the two numbers are Not relativly prime
            anwser = "Non Existant"
            print("There is no Multiplicative Inverse for those numbers")
            return render_template('index.html', nummy=nummy,moddy=moddy,anwser=anwser)
        else:
            anwser = modinv(nummy,moddy)
            print("The multiplicative inverse of {} under {} is: {}".format(nummy,moddy,anwser))
            return render_template('index.html', nummy=nummy,moddy=moddy,anwser=anwser)
    else: 
        return render_template('index') # its a GET request. no form submitted

@app.route('/modEasy', methods=['GET', 'POST'])
def modEasy():
    if request.method == 'POST':
        num = int(request.form['nums'])
        mod = int(request.form['moddy'])
        q = math.floor(num/mod)
        remain = num - (q*mod)
        print("The remainder of {} mod {} is: {}".format(num,mod,remain))

        return redirect(url_for('index'))
    return render_template('index') #GET Request

@app.route('/fastExpo', methods=['GET', 'POST'])  
def fastExpo():
    if request.method == 'POST':
        x = int(request.form['x'])
        e = int(request.form['e'])
        mod = int(request.form['modExpo'])
        remainder = FastModExo(x,e,mod)
        print("{} ^ {} mod {} is: {}".format(x,e,mod,remainder))
        return render_template('index.html', xx=x,ee=e,mm=mod,remainder=remainder)
    return render_template('index.html') # its a GET request. no form submitted

@app.route('/roots', methods=['GET', 'POST'])
def roots():
    if request.method == 'POST':
        modulo = int(request.form['nroots'])
        print("The smallest Primitive root is: {}".format(findPrimitive(modulo)))
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/rootsList', methods=['GET', 'POST'])
def rootsList():
    if request.method == 'POST':
        modulo = int(request.form['listroots'])
        print("The Primitive Roots are: {}".format(primRoots(modulo)))
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/prime', methods=['GET', 'POST'])
def prime():
    if request.method == 'POST':
        n = int(request.form['n'])
        res = isPrimeMR(n)
        if(isPrimeMR(n)):
            #Should be a prime number
            print('{} is a prime number'.format(n))
        else:
            print('{} is not a prime number'.format(n))
        return render_template('index.html',pis=n,res=res)
    return render_template('index') # its a GET request. no form submitted


@app.route('/primeFactorRoute', methods=['GET', 'POST'])
def primeFactorRoute():
    if request.method == 'POST':
        n = int(request.form['nFactor'])
        primeFactor(n)
        return redirect(url_for('index'))
    return render_template('index') # its a GET request. no form submitted


@app.route('/size', methods=['GET', 'POST'])
def size():
    """This function will take an integer as input from the user and print out a list
    of all the elements of Zn multiplicative group. The elements of this set are of course the numbers
    from 1-> n-1 that are reletively prime to n. """
    if request.method == 'POST':
        zn = int(request.form['n'])
        size = Order(zn)
        print("The order of {} is: {}".format(zn,Order(zn)))
        return render_template('index.html',size=size)
    
    return render_template('index.html')# GET Request

@app.route('/log', methods=['GET','POST'])
def log():
    if request.method == 'POST':
        x = int(request.form['x'])
        base = int(request.form['base'])
        result = math.log(x,base)
        print(result)
        print("The log of {} base {} is: {}".format(x,base,result))
        return redirect(url_for('index'))
    
    return render_template('index')# GET Request

@app.route('/baby', methods=['GET', 'POST'])
def baby():
    if request.method == 'POST':
        x = int(request.form['babyx'])
        basebaby = int(request.form['babybase'])
        babyMod = int(request.form['babyMod'])
        #babyStep(g,h,p)
        print(babyStep(x,basebaby,babyMod)) 
        #8942
        #print(x,basebaby,babyMod)
        #print(bsgs(x,basebaby,babyMod))
        return redirect(url_for('index'))
    return render_template('index')# GET Request

@app.route('/randP', methods=['GET', 'POST'])
def randP():
    if request.method == 'POST':
        rand = gen_random_prime()
        return render_template('index.html', rand=rand)
    return render_template('index.html')# GET Request
#####################################################################################
# Routes for performing ElGamal Encryption/Decryption on Strings
#####################################################################################
@app.route('/elEnc', methods=['GET','POST'])
def elEnc():
    if request.method == 'POST':
        msg = request.form['message']
        pkb = int(request.form['pub_bob'])
        b = int(request.form['generator'])
        pri_A = int(request.form['pri_A'])
        group = int(request.form['group'])
        print("This is in routes. The message is {} ".format(msg))
        print("Bob Public: {}".format(pkb))
        print("Generator: {}".format(b))
        print("Alice Private Key: {}".format(pri_A))
        print("Group used: {}".format(group))
        enc = encrypt(msg,pkb,pri_A,group) # Should return an encrypted message
        #Call the ElGamal Script to generate the Keys and encrypt the message
        return render_template('elGamalEnc.html', msg=msg, mod=group, pub_bob=pkb, msg_enc=enc)
    return render_template('elGamalEnc.html') #GET Request

@app.route('/elDec', methods=['GET','POST'])
def elDec():
    if request.method == 'POST':
        msg_enc = request.form['msg_enc'] #Will be a string of multiple numbers
        split = msg_enc.split(" ")
        print(type(split))
        print(split)
        split = list(map(int, split)) #Map the string elsements to Ints
        print(split)
        pka = int(request.form['pub_alice'])
        pri_B = int(request.form['pri_B'])
        p = int(request.form['g'])
        dec = decrypt(split,pka,pri_B,p)
        #dec = decrypt(msg_enc,pka,pri_B,p)
        return render_template('elGamalEnc.html', msg_enc=msg_enc,msg_dec=dec)
    return render_template('elGamalEnc.html') #GET Request

###################################################################################
# Routes for performing ElGamal Encryption/Decryption on Numbers
###################################################################################
@app.route('/elEncNum', methods=['GET','POST'])
def elEncNum():
    if request.method == 'POST':
        x = int(request.form['NumMessage'])
        pkb = int(request.form['pub_bob_num'])
        b = int(request.form['generator_num'])
        pri_A = int(request.form['pri_A_num'])
        group = int(request.form['group_num'])
        print("This is in routes. The message is {} ".format(x))
        print("Bob Public: {}".format(pkb))
        print("Generator: {}".format(b))
        print("Alice Private Key: {}".format(pri_A))
        print("Group used: {}".format(group))
        enc = encrypt_num(x,pkb,pri_A,group) # Should return an encrypted message
        #Call the ElGamal Script to generate the Keys and encrypt the message
        return render_template('elGamalEnc.html', num=x, mod_num=group, pub_bob_num=pkb, num_enc=enc)
    return render_template('elGamalEnc.html') #GET Request

@app.route('/elDecNum', methods=['GET','POST'])
def elDecNum():
    if request.method == 'POST':
        num_enc = int(request.form['num_enc']) #Will be a number
        pka = int(request.form['pub_alice_num'])
        pri_B = int(request.form['pri_B_num'])
        p = int(request.form['g_num'])
        dec = decrypt_num(num_enc,pka,pri_B,p)
        #dec = decrypt(msg_enc,pka,pri_B,p)
        return render_template('elGamalEnc.html', num_enc=num_enc,num_dec=dec)
    return render_template('elGamalEnc.html') #GET Request
###########################################################################
# Routes for ElGamal Key Generation
###########################################################################

@app.route('/elKeyGen', methods=['GET','POST'])
def elKeyGen():
    if request.method == 'POST':
        p = int(request.form['keygroup'])
        print('The Modulus is: {}'.format(p))
        keys_A = key_gen(p) #should return a dictionary
        pri_A = keys_A['PrivateKey']
        pub_A = keys_A['PublicKey']
        pubB = pub_A.get_b()
        pubH = pub_A.get_h()
        pubP = pub_A.get_p()
        priA = pri_A.get_r()
        print(pri_A)
        print(pub_A.get_h())
        keys_B = key_gen(p) #Keys for Bob
        bob_pri = keys_B['PrivateKey']
        bob_pub = keys_B['PublicKey']
        bobB, bobH, bobP, bobL = bob_pub.get_b(), bob_pub.get_h(), bob_pub.get_p(), bob_pri.get_r() # The Key info for Bob
        #print(keys)
        #print(keys.values())
        #print(keys['PublicKey'].get_p)
        #Call the ElGamal Script to generate the Keys and encrypt the message
        #return redirect(url_for('index'))
        return render_template('elGamalEnc.html', p=pubP, b=pubB, h=pubH, r=priA, bb=bobB, pb=bobP, hb=bobH, l=bobL)
    return render_template('elGamalEnc.html') #GET Request

@app.route('/elKeyGenRoot', methods=['GET','POST'])
def elKeyGenRoot():
    """Used if you already know a Primitive Root you want to use"""
    if request.method == 'POST':
        p = int(request.form['keygroupRoot'])
        b = int(request.form['Root'])
        print('The Modulus is: {}'.format(p))
        print('The Root is: {}'.format(b))
        keys_A = key_gen_root(p,b) #should return a dictionary
        pri_A = keys_A['PrivateKey']
        pub_A = keys_A['PublicKey']
        pubB = pub_A.get_b()
        pubH = pub_A.get_h()
        pubP = pub_A.get_p()
        priA = pri_A.get_r()
        print(pri_A)
        print(pub_A.get_h())
        keys_B = key_gen_root(p,b) #Keys for Bob
        bob_pri = keys_B['PrivateKey']
        bob_pub = keys_B['PublicKey']
        bobB, bobH, bobP, bobL = bob_pub.get_b(), bob_pub.get_h(), bob_pub.get_p(), bob_pri.get_r() # The Key info for Bob
        return render_template('elGamalEnc.html', pR=pubP, bR=pubB, hR=pubH, rR=priA)
    return render_template('elGamalEnc.html') #GET Request
###########################################################################
# Routes for RSA Key Generation - Either given p&q or randomlly generate prime p&q
###########################################################################

@app.route('/rsa_gen', methods=['GET','POST'])
def rsa_gen():
    print("In RSA")
    if request.method == 'POST':
        p = int(request.form['p1check'])
        q = int(request.form['q1check'])
        if not (isPrimeMR(p) and isPrimeMR(q)):
            print("both p and q must be prime")
            return render_template('rsa.html')
        #can safely assume the p & q entered are Prime
        keys = rsa_keys(p,q)
        e,d,n = keys["EncKey"].get_e(),keys["DecKey"].get_d(),keys["EncKey"].get_n()
        print("In RoutesRSA: ")
        print("Public Key: ({},{})".format(e,n))
        print("Private Key: ({},{})".format(d,n))
        return render_template('rsa.html', e=e,d=d,n=n)
    return render_template('rsa.html')# GET Request

@app.route('/rsa_gen_random', methods=['GET','POST'])
def rsa_gen_random():
    print("In RSA Random")
    if request.method == 'POST':
        p = gen_random_prime()
        q = gen_random_prime()
        keys = rsa_keys(p,q)
        e,d,n = keys["EncKey"].get_e(),keys["DecKey"].get_d(),keys["EncKey"].get_n()
        return render_template('rsa.html', e=e,d=d,n=n)
    return render_template('rsa.html')# GET Request

###########################################################################
# Routes for RSA Encryption/Decryption of Numbers
###########################################################################

@app.route('/rsa_enc_view', methods=['GET','POST'])
def rsa_enc_view():
    print("In RSA Encryption")
    if request.method == 'POST':
        print("POST ENC")
        num = int(request.form['rsa_num_enc'])
        e = int(request.form['e_enc'])
        n = int(request.form['n_enc'])
        enc = rsa_enc(num,e,n)
        return render_template('rsa.html', e_enc=e,rsa_enc=enc,n_enc=n)
    return render_template('rsa.html')# GET Request

@app.route('/rsa_dec_view', methods=['GET','POST'])
def rsa_dec_view():
    print("In RSA Decryption")
    if request.method == 'POST':
        print("POST DEC")
        num = int(request.form['rsa_num_dec'])
        d = int(request.form['d_dec'])
        n = int(request.form['n_dec'])
        print("enc: {}, d = {}, n = {}".format(num,d,n))
        dec = rsa_dec(num,d,n)
        return render_template('rsa.html', d_dec=d,rsa_dec=dec,n_dec=n)
    return render_template('rsa.html')# GET Request