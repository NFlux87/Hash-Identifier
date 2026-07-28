from typing import Literal
"""
Create list of Prefix-Rules
 # format
    |prefix|name|discribe|
"""
Confidence = Literal["High", "Medium", "Low"]

PREFIX_RULES: list[tuple[str, str, str]] = [
    # ------------------------------------------------------------------
    # PHC / modern password hashing
    # ------------------------------------------------------------------
    ("$argon2id$", "Argon2id", "PHC string; hybrid Argon2 variant"),
    ("$argon2i$", "Argon2i", "PHC string; data-independent Argon2 variant"),
    ("$argon2d$", "Argon2d", "PHC string; data-dependent Argon2 variant"),
    ("$scrypt$", "scrypt", "scrypt encoded password hash"),
    ("$7$", "scrypt crypt", "scrypt modular-crypt format"),
    ("$y$", "yescrypt", "yescrypt modular-crypt format"),
    ("$gy$", "gost-yescrypt", "GOST yescrypt modular-crypt format"),

    # ------------------------------------------------------------------
    # bcrypt and wrappers
    # ------------------------------------------------------------------
    ("$bcrypt-sha256$", "bcrypt-SHA256", "Passlib bcrypt SHA-256 wrapper"),
    ("$2b$", "bcrypt", "Current OpenBSD bcrypt revision"),
    ("$2y$", "bcrypt", "bcrypt revision commonly emitted by PHP"),
    ("$2x$", "bcrypt", "bcrypt compatibility revision"),
    ("$2a$", "bcrypt", "Legacy bcrypt revision"),
    ("$2$", "bcrypt", "Original bcrypt revision"),

    # ------------------------------------------------------------------
    # Unix crypt / modular crypt
    # ------------------------------------------------------------------
    ("$apr1$", "Apache apr1-MD5", "Apache htpasswd MD5-crypt variant"),
    ("$1$", "MD5-crypt", "Unix MD5-crypt; also Cisco type 5 encoding"),
    ("$5$", "SHA256-crypt", "Unix SHA-256 crypt"),
    ("$6$", "SHA512-crypt", "Unix SHA-512 crypt"),
    ("$sha1$", "SHA1-crypt", "NetBSD-style SHA-1 crypt"),
    ("$md5$", "Sun MD5-crypt", "Solaris SunMD5 password hash"),
    ("$md5,", "Sun MD5-crypt", "Solaris SunMD5 rounds form"),
    ("$3$", "BSD NT hash", "FreeBSD-style NT hash wrapper"),
    ("_", "BSDi crypt", "Extended DES / BSDi crypt"),

    # ------------------------------------------------------------------
    # PBKDF2 / Passlib
    # ------------------------------------------------------------------
    ("$pbkdf2-sha512$", "PBKDF2-HMAC-SHA512", "Passlib modular PBKDF2"),
    ("$pbkdf2-sha256$", "PBKDF2-HMAC-SHA256", "Passlib modular PBKDF2"),
    ("$pbkdf2-sha1$", "PBKDF2-HMAC-SHA1", "Passlib modular PBKDF2"),
    ("$pbkdf2$", "PBKDF2", "Generic Passlib PBKDF2 format"),
    ("$p5k2$", "PBKDF2", "CTA / Cryptacular PBKDF2 format"),
    ("$scram$", "SCRAM", "Passlib SCRAM multi-digest format"),

    # ------------------------------------------------------------------
    # PHP / CMS
    # ------------------------------------------------------------------
    ("$P$", "phpass", "Portable PHP password hash; WordPress and others"),
    ("$H$", "phpass", "phpBB alternate phpass prefix"),
    ("$S$", "Drupal 7", "Drupal SHA-512 based password hash"),
    ("$Q$", "Drupal", "Drupal-compatible phpass-derived format"),
    ("$wp$", "WordPress bcrypt", "Newer WordPress bcrypt password format"),
    ("$dynamic_", "John dynamic format", "John the Ripper dynamic hash syntax"),

    # ------------------------------------------------------------------
    # Django and common frameworks
    # ------------------------------------------------------------------
    ("pbkdf2_sha256$", "Django PBKDF2-SHA256", "Django password hasher"),
    ("pbkdf2_sha1$", "Django PBKDF2-SHA1", "Legacy Django password hasher"),
    ("bcrypt_sha256$", "Django bcrypt-SHA256", "Django bcrypt SHA-256 wrapper"),
    ("bcrypt$", "Django bcrypt", "Django bcrypt password hasher"),
    ("argon2$", "Django Argon2", "Django Argon2 password hasher"),
    ("scrypt$", "Django scrypt", "Django scrypt password hasher"),
    ("sha1$", "Django salted SHA-1", "Legacy Django salted SHA-1"),
    ("md5$", "Django salted MD5", "Legacy Django salted MD5"),
    ("unsalted_sha1$", "Django unsalted SHA-1", "Legacy Django format"),
    ("unsalted_md5$", "Django unsalted MD5", "Legacy Django format"),

    # Werkzeug / Flask-style strings
    ("pbkdf2:", "Werkzeug PBKDF2", "Werkzeug generate_password_hash format"),
    ("scrypt:", "Werkzeug scrypt", "Werkzeug generate_password_hash format"),

    # ------------------------------------------------------------------
    # LDAP / directory formats
    # ------------------------------------------------------------------
    ("{SSHA512}", "LDAP SSHA-512", "Salted SHA-512 LDAP password"),
    ("{SHA512}", "LDAP SHA-512", "SHA-512 LDAP password"),
    ("{SSHA384}", "LDAP SSHA-384", "Salted SHA-384 LDAP password"),
    ("{SHA384}", "LDAP SHA-384", "SHA-384 LDAP password"),
    ("{SSHA256}", "LDAP SSHA-256", "Salted SHA-256 LDAP password"),
    ("{SHA256}", "LDAP SHA-256", "SHA-256 LDAP password"),
    ("{SSHA}", "LDAP SSHA-1", "Salted SHA-1 LDAP password"),
    ("{SHA}", "LDAP SHA-1", "SHA-1 LDAP password"),
    ("{SMD5}", "LDAP salted MD5", "Salted MD5 LDAP password"),
    ("{MD5}", "LDAP MD5", "MD5 LDAP password"),
    ("{CRYPT}", "LDAP crypt", "LDAP wrapper around system crypt format"),
    ("{CLEARTEXT}", "LDAP cleartext", "Cleartext LDAP scheme; not a hash"),

    # ------------------------------------------------------------------
    # AIX password formats
    # ------------------------------------------------------------------
    ("{smd5}", "AIX smd5", "AIX salted MD5 password format"),
    ("{ssha1}", "AIX ssha1", "AIX salted SHA-1 password format"),
    ("{ssha256}", "AIX ssha256", "AIX salted SHA-256 password format"),
    ("{ssha512}", "AIX ssha512", "AIX salted SHA-512 password format"),

    # ------------------------------------------------------------------
    # Cisco / network devices
    # ------------------------------------------------------------------
    ("$8$", "Cisco type 8", "Cisco PBKDF2-SHA256 password hash"),
    ("$9$", "Cisco type 9", "Cisco scrypt password hash"),
    ("$4$", "Cisco type 4", "Legacy Cisco SHA-256 password hash"),
    ("$cisco4$", "Cisco type 4", "Cisco type 4 tagged representation"),
    ("$vnc$", "VNC", "VNC challenge-response extracted hash"),
    ("$sip$", "SIP digest authentication", "SIP digest extracted hash"),
    ("$SNMPv3$", "SNMPv3", "SNMPv3 authentication hash format"),
    ("$netntlm$", "NetNTLMv1", "Windows NTLM challenge-response v1"),
    ("$NETNTLMv2$", "NetNTLMv2", "Windows NTLM challenge-response v2"),

    # ------------------------------------------------------------------
    # Windows / Microsoft
    # ------------------------------------------------------------------
    ("$DCC2$", "MS Cache 2", "Domain Cached Credentials v2"),
    ("$NT$", "NTLM", "Tagged NT hash"),
    ("$LM$", "LM", "Tagged LAN Manager hash"),
    ("$bitlocker$", "BitLocker", "BitLocker recovery/password hash"),
    ("$efs$", "Windows EFS", "Windows Encrypting File System hash"),
    ("$krb5pa$23$", "Kerberos 5 AS-REQ etype 23", "Kerberos pre-authentication"),
    ("$krb5pa$17$", "Kerberos 5 AS-REQ etype 17", "Kerberos AES128 pre-auth"),
    ("$krb5pa$18$", "Kerberos 5 AS-REQ etype 18", "Kerberos AES256 pre-auth"),
    ("$krb5tgs$23$", "Kerberos 5 TGS etype 23", "Kerberoast RC4-HMAC ticket"),
    ("$krb5tgs$17$", "Kerberos 5 TGS etype 17", "Kerberoast AES128 ticket"),
    ("$krb5tgs$18$", "Kerberos 5 TGS etype 18", "Kerberoast AES256 ticket"),
    ("$krb5asrep$23$", "Kerberos 5 AS-REP etype 23", "AS-REP roast RC4-HMAC"),
    ("$krb5asrep$17$", "Kerberos 5 AS-REP etype 17", "AS-REP roast AES128"),
    ("$krb5asrep$18$", "Kerberos 5 AS-REP etype 18", "AS-REP roast AES256"),

    # ------------------------------------------------------------------
    # Databases
    # ------------------------------------------------------------------
    ("$mysqlna$", "MySQL network authentication", "MySQL challenge-response"),
    ("$mysql-sha1$", "MySQL SHA-1", "Tagged MySQL 4.1+ password hash"),
    ("$postgres$", "PostgreSQL", "Tagged PostgreSQL password hash"),
    ("SCRAM-SHA-256$", "PostgreSQL SCRAM-SHA-256", "PostgreSQL SCRAM verifier"),
    ("S:", "Oracle 11g", "Oracle 11g SHA-1 verifier form"),
    ("T:", "Oracle 12c", "Oracle 12c PBKDF2 verifier component"),
    ("H:", "Oracle H", "Oracle 7+ DES verifier form"),

    # MySQL native hashes require a full regex because '*' alone is weak.
    ("*", "MySQL 4.1+ SHA-1", "Candidate only; validate as '*' plus 40 hex chars"),

    # ------------------------------------------------------------------
    # Archives
    # ------------------------------------------------------------------
    ("$7z$", "7-Zip", "7-Zip archive password hash"),
    ("$zip2$", "WinZip", "WinZip AES archive hash"),
    ("$pkzip2$", "PKZIP", "PKZIP archive hash"),
    ("$pkzip$", "PKZIP", "PKZIP archive hash"),
    ("$rar5$", "RAR5", "RAR version 5 archive hash"),
    ("$RAR3$", "RAR3", "RAR version 3 archive hash"),
    ("$rar3$", "RAR3", "RAR version 3 archive hash"),
    ("$zip3$", "SecureZIP", "SecureZIP archive hash"),
    ("$axcrypt$", "AxCrypt", "AxCrypt encrypted-file hash"),
    ("$ansible$", "Ansible Vault", "Ansible Vault encrypted data"),
    ("$ansible$0$", "Ansible Vault", "Ansible Vault format"),
    ("$mozilla$", "Mozilla key database", "Firefox/Thunderbird master password"),

    # ------------------------------------------------------------------
    # Documents and password managers
    # ------------------------------------------------------------------
    ("$office$", "Microsoft Office", "Office document password hash"),
    ("$oldoffice$", "Legacy Microsoft Office", "Office 97-2003 password hash"),
    ("$pdf$", "PDF", "PDF document password hash"),
    ("$keepass$", "KeePass", "KeePass database password hash"),
    ("$pwsafe$", "Password Safe", "Password Safe database hash"),
    ("$lastpass$", "LastPass", "LastPass vault-derived hash"),
    ("$1password$", "1Password", "1Password vault hash"),
    ("$enpass$", "Enpass", "Enpass password manager database"),
    ("$money$", "MS Money", "Microsoft Money password hash"),

    # ------------------------------------------------------------------
    # Disk / container encryption
    # ------------------------------------------------------------------
    ("$veracrypt$", "VeraCrypt", "VeraCrypt volume hash"),
    ("$truecrypt$", "TrueCrypt", "TrueCrypt volume hash"),
    ("$luks$", "LUKS", "Linux Unified Key Setup hash"),
    ("$fvde$", "FileVault 2", "Apple FileVault 2 hash"),
    ("$fvde$1$", "FileVault 2", "Apple FileVault 2 format"),
    ("$dmg$", "Apple DMG", "Encrypted Apple disk image"),
    ("$zfs$", "ZFS", "ZFS native encryption hash"),

    # ------------------------------------------------------------------
    # Cryptocurrency wallets
    # ------------------------------------------------------------------
    ("$bitcoin$", "Bitcoin wallet", "Bitcoin wallet.dat extracted hash"),
    ("$ethereum$", "Ethereum wallet", "Ethereum keystore extracted hash"),
    ("$electrum$", "Electrum wallet", "Electrum wallet password hash"),
    ("$metamask$", "MetaMask", "MetaMask vault extracted hash"),
    ("$monero$", "Monero wallet", "Monero wallet extracted hash"),
    ("$dogechain$", "Dogechain wallet", "Dogechain wallet hash"),
    ("$blockchain$", "Blockchain.com wallet", "Blockchain wallet hash"),

    # ------------------------------------------------------------------
    # Apple / mobile
    # ------------------------------------------------------------------
    ("$ml$", "Apple Secure Notes", "Apple Notes password hash"),
    ("$itunes_backup$", "iTunes backup", "Encrypted iOS backup hash"),
    ("$mobilekeychain$", "Apple Keychain", "Apple mobile keychain hash"),
    ("$keychain$", "Apple Keychain", "macOS keychain hash"),
    ("$androidbackup$", "Android backup", "Android backup password hash"),
    ("$fde$", "Android FDE", "Android full-disk encryption hash"),

    # ------------------------------------------------------------------
    # Application-specific formats
    # ------------------------------------------------------------------
    ("$telegram$", "Telegram Desktop", "Telegram local data password hash"),
    ("$signal$", "Signal", "Signal local database/password hash"),
    ("$skype$", "Skype", "Skype password hash format"),
    ("$discord$", "Discord", "Extracted Discord-related credential format"),
    ("$mongodb-scram$", "MongoDB SCRAM", "MongoDB SCRAM verifier"),
    ("$mongodb$", "MongoDB", "MongoDB authentication hash"),
    ("$elastic$", "Elasticsearch", "Elasticsearch password hash"),
    ("$grub.pbkdf2.sha512$", "GRUB2 PBKDF2-SHA512", "GRUB2 boot password"),
    ("grub.pbkdf2.sha512.", "GRUB2 PBKDF2-SHA512", "GRUB2 boot password"),
    ("$ecryptfs$", "eCryptfs", "Linux eCryptfs wrapped passphrase"),
    ("$gpg$", "GPG private key", "GnuPG private-key password hash"),
    ("$sshng$", "SSH private key", "John/hashcat SSH key extracted hash"),
    ("$ssh$", "SSH private key", "SSH private-key extracted hash"),
    ("$putty$", "PuTTY private key", "PuTTY PPK extracted hash"),

    # ------------------------------------------------------------------
    # Misc tagged raw digests
    # ------------------------------------------------------------------
    ("$md4$", "MD4", "Tagged raw MD4 digest"),
    ("$md5$", "MD5", "Tagged raw MD5 digest; may collide with SunMD5"),
    ("$sha1$", "SHA-1", "Tagged raw SHA-1; may collide with SHA1-crypt"),
    ("$sha224$", "SHA-224", "Tagged raw SHA-224 digest"),
    ("$sha256$", "SHA-256", "Tagged raw SHA-256 digest"),
    ("$sha384$", "SHA-384", "Tagged raw SHA-384 digest"),
    ("$sha512$", "SHA-512", "Tagged raw SHA-512 digest"),
    ("$ripemd$", "RIPEMD", "Tagged RIPEMD-family digest"),
    ("$haval$", "HAVAL", "Tagged HAVAL-family digest"),
    ("$snefru$", "Snefru", "Tagged Snefru digest"),
    ("$whirlpool$", "Whirlpool", "Tagged Whirlpool digest"),
    ("$crc32$", "CRC-32", "Tagged CRC-32 checksum"),
]


# Length Only
# for raw Hash in Hexdecimal
RAW_HEX_RULES: dict[int, tuple[tuple[str, str], ...]] = {
    8: (("CRC-32", "32-bit hexadecimal checksum"),),
    16: (("MySQL 3.23", "Legacy MySQL 64-bit password hash"),),
    32: (
        ("MD4", "128-bit hexadecimal digest"),
        ("MD5", "128-bit hexadecimal digest"),
        ("NTLM", "128-bit hexadecimal digest"),
    ),
    40: (
        ("SHA-1", "160-bit hexadecimal digest"),
        ("RIPEMD-160", "160-bit hexadecimal digest"),
    ),
    56: (
        ("SHA-224", "224-bit hexadecimal digest"),
        ("SHA3-224", "224-bit hexadecimal digest"),
    ),
    64: (
        ("SHA-256", "256-bit hexadecimal digest"),
        ("SHA3-256", "256-bit hexadecimal digest"),
        ("BLAKE2s-256", "256-bit hexadecimal digest"),
    ),
    96: (
        ("SHA-384", "384-bit hexadecimal digest"),
        ("SHA3-384", "384-bit hexadecimal digest"),
    ),
    128: (
        ("SHA-512", "512-bit hexadecimal digest"),
        ("SHA3-512", "512-bit hexadecimal digest"),
        ("BLAKE2b-512", "512-bit hexadecimal digest"),
        ("Whirlpool", "512-bit hexadecimal digest"),
    ),
}


# Full-format validators. A matching prefix gives Low confidence; a complete
# match here upgrades the candidate to High confidence.
# Format: (algorithm, regular expression)
FULL_FORMAT_RULES: list[tuple[str, str]] = [
    # bcrypt: revision, cost 04-31, then exactly 53 bcrypt-base64 characters.
    ("bcrypt", r"\$2[abxy]\$(?:0[4-9]|[12][0-9]|3[01])\$[./A-Za-z0-9]{53}"),

    # Common PHC formats.
    (
        "Argon2id",
        r"\$argon2id\$v=\d+\$m=\d+,t=\d+,p=\d+\$[A-Za-z0-9+/]+={0,2}\$[A-Za-z0-9+/]+={0,2}",
    ),
    (
        "Argon2i",
        r"\$argon2i\$v=\d+\$m=\d+,t=\d+,p=\d+\$[A-Za-z0-9+/]+={0,2}\$[A-Za-z0-9+/]+={0,2}",
    ),
    (
        "Argon2d",
        r"\$argon2d\$v=\d+\$m=\d+,t=\d+,p=\d+\$[A-Za-z0-9+/]+={0,2}\$[A-Za-z0-9+/]+={0,2}",
    ),

    # Unix modular crypt formats.
    ("MD5-crypt", r"\$1\$[./A-Za-z0-9]{1,8}\$[./A-Za-z0-9]{22}"),
    (
        "SHA256-crypt",
        r"\$5\$(?:rounds=\d+\$)?[./A-Za-z0-9]{1,16}\$[./A-Za-z0-9]{43}",
    ),
    (
        "SHA512-crypt",
        r"\$6\$(?:rounds=\d+\$)?[./A-Za-z0-9]{1,16}\$[./A-Za-z0-9]{86}",
    ),

    # Database and framework formats.
    ("MySQL 4.1+ SHA-1", r"\*[0-9A-Fa-f]{40}"),
    ("Django unsalted MD5", r"unsalted_md5\$[0-9A-Fa-f]{32}"),
    ("Django unsalted SHA-1", r"unsalted_sha1\$[0-9A-Fa-f]{40}"),
    ("Django salted MD5", r"md5\$[^$]+\$[0-9A-Fa-f]{32}"),
    ("Django salted SHA-1", r"sha1\$[^$]+\$[0-9A-Fa-f]{40}"),
    (
        "Django PBKDF2-SHA256",
        r"pbkdf2_sha256\$\d+\$[^$]+\$[A-Za-z0-9+/]+={0,2}",
    ),
    (
        "Django PBKDF2-SHA1",
        r"pbkdf2_sha1\$\d+\$[^$]+\$[A-Za-z0-9+/]+={0,2}",
    ),

    # Tagged raw hexadecimal digests.
    ("MD4", r"\$md4\$[0-9A-Fa-f]{32}"),
    ("MD5", r"\$md5\$[0-9A-Fa-f]{32}"),
    ("SHA-1", r"\$sha1\$[0-9A-Fa-f]{40}"),
    ("SHA-224", r"\$sha224\$[0-9A-Fa-f]{56}"),
    ("SHA-256", r"\$sha256\$[0-9A-Fa-f]{64}"),
    ("SHA-384", r"\$sha384\$[0-9A-Fa-f]{96}"),
    ("SHA-512", r"\$sha512\$[0-9A-Fa-f]{128}"),
    ("Whirlpool", r"\$whirlpool\$[0-9A-Fa-f]{128}"),
    ("CRC-32", r"\$crc32\$[0-9A-Fa-f]{8}"),
]
