# SiguriaEteDhenave_TOTP_gr8

TOTP Authentication Application

Ky projekt është një aplikacion për autentikim me Time-Based One-Time Password (TOTP) që implementon siguri me dy faktorë (2FA) duke përdorur kode njëpërdorimshe të gjeneruara çdo 30 sekonda. Aplikacioni përfshin edhe gjenerimin dhe paraqitjen e QR Code, duke e bërë konfigurimin më të lehtë në aplikacione autentikuese si Google Authenticator.

Karakteristikat:
-Gjenerimi i kodeve TOTP sipas standardit RFC 6238
-Regjistrim dhe autentikim i përdoruesve
-Gjenerim dhe shfaqje e QR Code
-Verifikim i kodeve në kohë reale
-Integrim me aplikacione autentikuese
-Ruajtje e sigurt e secret key dhe kredencialeve
-Teknologjitë e përdorura
-Python
-PyOTP
-QRCode
-Console Interface

Si funksionon:
-Përdoruesi regjistrohet në sistem.
-Sistemi gjeneron një secret key unik për përdoruesin.
-Gjenerohet një QR Code që përmban informacionin TOTP.
-Përdoruesi e skanon QR Code me një aplikacion autentikues.
-Aplikacioni gjeneron kode të reja çdo 30 sekonda.
-Kodi verifikohet nga sistemi gjatë login-it.

Qëllimi i projektit:

Qëllimi i këtij projekti është të demonstrojë implementimin praktik të autentikimit me dy faktorë duke përdorur TOTP dhe QR Code për të rritur sigurinë e sistemeve dhe aplikacioneve moderne.

Autor: Erion Meshi, Zymer Ahmetaj, Erijon Elshani, Erion Qerimi
