# -*- coding: utf-8 -*-
"""
    encriptacion.gen_keys
    ~~~~~~~~~~~~~~~~~~~~~

    Genera un par de llaves publicas y privadas y las instala en
    el anillo de llaves del usuario.

    :license: GPL2
    Copyright © 2023 Jaime Andres Feldman Budnik
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.
    , see LICENSE for more details.
"""

import gnupg
import os, sys

# Obteniendo el directorio el directorio de usuairo.
homedir = os.path.expanduser('~')

# Inicializando gnupg con el llavero en la carpeta del usuario.

# En GNU/Linux Manajro funciona de esta forma.
gpg = gnupg.GPG(gpgbinary='/usr/bin/gpg')
# os.popen("which gpg").read().strip()

# gpg = gnupg.GPG(homedir + '/.gnupg')

gpg.encoding = 'utf-8'
input_data = gpg.gen_key_input(
    name_email = 'alice@cuper.org',
    passphrase = 'mypassphrase',
    key_type = 'RSA',
    key_length = 2048)

key = gpg.gen_key(input_data)
print(key)

