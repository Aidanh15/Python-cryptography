#Public key generator (RSA) cryptography
#Code to generate pub and priv keys as per the RSA algorithm, note: not fully secure due to pseudorandom number generation as opposed to true random
import random, sys, os, primeNum,cryptomath

def main():
    # Create pub/priv key pair with 1024-bit keys.
    print('Making key files..')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files created.')

def generateKey(keySize):
    #creates a pub/priv keys keySize bits in size
    p = 0
    q = 0
    # 1) Create two primes p and q, find n = p*q.
    print('Generating p prime')
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
        n = p*q

    #2) Create number e that is relatvely prime to (p-1)*(q-1)
    print('Making e that us relatively prime to (p-1)(q-1)')
    while True:
        e = random.randrange(2 ** (keySize-1), 2 ** (keySize))
        if cryptomath.gcd(e, (p-1) * (q-1)) == 1:
            break

    #3) Calc the mod inverse of e:
    print('Calculating d, the mod inverse of e.')
    d = cryptomath.findModInverse(e, (p-1)*(q-1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public Key:', publicKey)
    print('Private Key:', privateKey)

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    #creates two .txt files x_pubkey.tx, x_privkey.txt
    #also must prevent overwriting older key files

    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: the file %s_pubkey.txt or %s_privkey.txt already exists, use a different name or delete files to rerun' % (name, name)) 
    
    publicKey, privateKey = generateKey(keySize)
    print()

    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt..' % (name))
    fo = open('%s_pubkey.txt' %(name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    print()

    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt..' % (name))
    fo = open('%s_privkey.txt' %(name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()


# if generatekeys.py is run instead of imported as a module, call the main() function.

 #   if __name__ == '__main__':
      #  main()

#prin(t(generateKey(10))
print(main())
