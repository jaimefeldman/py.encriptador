# -*- coding: utf-8 -*-
"""
    encriptacion.gen_pass
    ~~~~~~~~~~~~~~~~~~~~~

    Generador de claves aleatorias.

    :copyright: (c) 2023 by yo.
    :license: GP2 gen_pass.py - Generandor de claves aleatorias
    Copyright © 2023 Jaime Feldman Budnik
    
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

import random
import string
import re

def genpass(password_lenght, chuncks) -> str:
    passphrase = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(password_lenght))
    # return passphrase
    regex = re.sub(r'((?:(?=(10|.))\2){' + f'{chuncks}' +'})(?!$)', r'\1-',passphrase)
    return regex 
