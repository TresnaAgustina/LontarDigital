class Rulebase:
    
    def __init__(self):
        self.HasilTrans = [""]
        self.IndexTrans = 0
        self.Value = 10
        self.Last = 0
        self.hasil_aksara = ""
        self.gantungan = 0
        self.cecek = 0
        self.katakhusus = 0


    def looping_teks(self, teks_latin):
        for_rulebase = teks_latin.lower() # asta
        num = len(for_rulebase) #4
        loop = 0
        
        self.HasilTrans = [""] * num
        self.IndexTrans = 0

        while self.IndexTrans <= num - 1:
            self.enkode(self.IndexTrans, for_rulebase)
            

        while loop <= num - 1:
            self.hasilaksara = "".join(self.HasilTrans)
            loop += 1

        return self.hasilaksara

    def enkode(self, x, teks):
        num = len(teks)
        karakter = teks[x]
        tempHrf1 = ""
        tempHrf2 = ""
        tempHrf3 = ""

        # ===***=== case a ===***=== 
        if karakter == 'a':
            # if huruf pertama
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'A'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'h'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                # end huruf pertama
            else:
                if teks[x - 1] == ' ':
                    # jika depannya spasi
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'A'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1

                        else:
                            self.HasilTrans[x] = 'h'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        #kata khusus
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'A'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[x] = 'h'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    #kata khusus baris ke-130
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/A'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == 'þ' or teks[x - 2] == '°'):
                        self.HasilTrans[x] = 'h'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1

                    else:
                        self.HasilTrans[x] = 'À'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    # end jika depannya spasi = baris ke-157

                    # baris ke-159
                elif (self.gantungan == 1 and teks[x - 1] == 'i'):
                    self.HasilTrans[x] = 'ê'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (self.gantungan == 1 and teks[x - 1] != 'a'):
                    self.HasilTrans[x] = ""
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'A'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    else:
                        self.HasilTrans[x] = 'h'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif teks[x - 1] == 'i':
                    self.HasilTrans[x] = 'ê'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/A'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1

                else:
                    self.HasilTrans[x] = ""
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        # ===***=== end case a ===***===  

        # ===***=== case b ===***=== 
        elif karakter == "b":
            if x == 0:
                self.HasilTrans[x] = 'b'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0

            else:
                if teks[x - 1] == ' ':
                    # depan spasi baris ke-242
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        self.HasilTrans[x] = 'b'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    #baris ke-253
                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'b'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'ã'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                    
                    elif (teks[x - 2] == ',' or teks[x - 2] == '.' or teks[x - 2] == ':' ):
                        self.HasilTrans[self.IndexTrans] = 'b'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    elif (teks[x - 2] == 'þ' or teks[x - 2] == '°'):
                        self.HasilTrans[x] = 'b'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'ã'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                        else:
                            self.HasilTrans[self.IndexTrans] = '/b'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    # end spasi depan baris ke-310
                
                # baris ke-312
                elif (teks[x - 1] =='.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.HasilTrans] = 'b'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'b'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'b'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'ã'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'ã'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    
                    else:
                        self.HasilTrans[self.IndexTrans] = '/b'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case b===***=== 

        # ===***=== case c ===***===  
        elif karakter == 'c':
            # huruf pertama
            if x == 0:
                self.HasilTrans[x] = 'c'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            # tidak ada huruf pertama
            else:
                # jika di depan spasi
                if teks[x - 1] ==' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'c'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'c'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ç'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0

                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'c'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Ç'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                        else:
                            self.HasilTrans[self.IndexTrans] = '/c'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # end jika depan spasi - baris ke-443

                # baris ke-445
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    self.HasilTrans[x] = 'c'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'c'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ç'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                #baris ke-471
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'c'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'Ç'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/c'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case c ===***===  

        # ===***=== case d ===***===  
        elif karakter == 'd':
            #jika di depan spasi
            if x == 0:
                #kata khusus
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'D'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'd'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

            # tidak ada huruf di depannya 527
            else:
                # depan spasi
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        #kata khusus
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'D'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'd'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    
                    elif teks[x - 2] == 'r':
                        # kata khusus
                        if (self.gantungan == 1 and teks[x + 1] == 'ÿ'):
                            self.HasilTrans[self.IndexTrans] = 'D'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        elif (self.gantungan == 1):
                            self.HasilTrans[self.IndexTrans] = 'd'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ñ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        #end baris 578

                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        # kata khusus
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'D'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'd'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = '/D'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Ñ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/d'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # end depan spasi 630

                # 632
                # my edit
                elif (teks[x + 1] == 'h'):
                    self.HasilTrans[self.IndexTrans] = 'a'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 0
                # end may edit
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    # kata khusus 636
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = 'D'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'd'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif teks[x - 1] == 'r':
                    # kata khusus 656
                    if (self.gantungan == 1 and teks[x + 1] == 'ÿ'):
                        self.HasilTrans[self.IndexTrans] = 'D'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'd'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ñ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                # 682
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    # kata khusus 685
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = 'D'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'd'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                # 703
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = '/D'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1

                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'Ñ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/d'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0         
        # ===***=== end case d ===***===         

        # ===***=== case e ===***===  
        elif karakter == 'e':
            if x == 0:
                self.HasilTrans[self.IndexTrans] = 'eh'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':

                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'eh'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'eh'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                        if self.gantungan == 1:

                            if (teks[x - 1] == 'r' and (self.IndexTrans - 3 != 0)):

                                if (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or teks[x - 1] == 'r' or self.cecek == 1):
                                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                    self.HasilTrans[self.IndexTrans] = tempHrf1
                                    self.IndexTrans = self.IndexTrans + 1
                                    self.gantungan = 0
                                    self.cecek = 0
                                else:
                                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                    tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                                    self.HasilTrans[self.IndexTrans] = 'e'
                                    self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                    self.HasilTrans[self.IndexTrans] = tempHrf1
                                    self.IndexTrans = self.IndexTrans + 1
                                    self.gantungan = 0
                                    self.cecek = 0

                            else:
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                self.HasilTrans[self.IndexTrans - 2] = 'e'
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                self.HasilTrans[self.IndexTrans] = tempHrf1
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0

                        elif (teks[x + 1] == '.' or teks[x + 1] == ',' or teks[x - 1] == ':'):
                            self.HasilTrans[self.IndexTrans] = 'eh'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans - 1] = 'e'
                            self.HasilTrans[self.IndexTrans] = tempHrf1
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'eh'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                elif (teks[x - 1] == 'g' and teks[x - 2] == 'n' and self.gantungan == 0):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 1]
                    self.HasilTrans[self.IndexTrans] = tempHrf2
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == 'y' and teks[x - 2] == 'n' and self.gantungan == 0):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 1]
                    self.HasilTrans[self.IndexTrans] = tempHrf2
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    if self.gantungan == 1:
                        if (teks[x - 1] == 'r' and (self.IndexTrans - 3 != 0)):
                            if (teks[x - 2] == 'g' and teks[x - 3] == 'n'):
                                tempHrf1 = self.HasilTrans[self.IndexTrans - 3]
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                tempHrf3 = self.HasilTrans[self.IndexTrans - 1]
                                self.HasilTrans[self.IndexTrans] = tempHrf3
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                self.HasilTrans[self.IndexTrans - 2] = tempHrf1
                                self.HasilTrans[self.IndexTrans - 3] = 'e'
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0
                            elif (teks[x - 3] == 'ī' or teks[x - 3] == 'ê' or teks[x - 3] == 'ú' or teks[x - 3] == 'ô' or teks[x - 3] == 'ā' or teks[x - 3] == 'â' or teks[x - 3] == 'ã' or teks[x - 3] == 'ä' or teks[x - 3] == 'ì' or teks[x - 3] == 'µ' or teks[x - 3] == 'a' or teks[x - 3] == 'i' or teks[x - 3] == 'u' or teks[x - 3] == 'e' or teks[x - 3] == 'o' or teks[x - 3] == 'é' or teks[x - 3] == 'h' or teks[x - 3] == 'r' or self.cecek == 1):
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                self.HasilTrans[self.IndexTrans - 2] = 'e'
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                self.HasilTrans[self.IndexTrans] = tempHrf1
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0
                            else:
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                                self.HasilTrans[self.IndexTrans] = 'e'
                                self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                self.HasilTrans[self.IndexTrans] = tempHrf1
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0
                        #921
                        elif (teks[x - 1] == 'g' and teks[x - 2] == 'n' and teks[x - 3] == 'a' and teks[x - 4] == 'i'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            self.HasilTrans[self.IndexTrans - 2] == 'e'
                            self.HasilTrans[self.IndexTrans - 1] == tempHrf2
                            self.HasilTrans[self.IndexTrans] == ''
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0 
                        elif (teks[x - 1] == 'y' and teks[x - 2] == 'n' and teks[x - 3] == 'a' and teks[x - 4] == 'i'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            self.HasilTrans[self.IndexTrans - 2] == 'e'
                            self.HasilTrans[self.IndexTrans - 1] == tempHrf2
                            self.HasilTrans[self.IndexTrans] == ''
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0 
                        # 950
                        elif (teks[x - 1] == 'g' and teks[x - 2] == 'n'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 4]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            tempHrf3 = self.HasilTrans[self.IndexTrans - 1]
                            self.HasilTrans[self.IndexTrans - 4] = 'e'
                            self.HasilTrans[self.IndexTrans - 2] = tempHrf1
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        elif (teks[x - 1] == 'y' and teks[x - 2] == 'n'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 4]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            tempHrf3 = self.HasilTrans[self.IndexTrans - 1]
                            self.HasilTrans[self.IndexTrans - 4] = 'e'
                            self.HasilTrans[self.IndexTrans - 2] = tempHrf1
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        # 981
                        elif (teks[x - 2] == 'g' and teks[x - 3] == 'n'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 3]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            tempHrf3 = self.HasilTrans[self.IndexTrans - 1]
                            self.HasilTrans[self.IndexTrans] = tempHrf3
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.HasilTrans[self.IndexTrans - 2] = tempHrf1
                            self.HasilTrans[self.IndexTrans - 3] = 'e'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        # 997
                        elif (teks[x - 2] == 'y' and teks[x - 3] == 'n'):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 3]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            tempHrf3 = self.HasilTrans[self.IndexTrans - 1]
                            self.HasilTrans[self.IndexTrans] = tempHrf3
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.HasilTrans[self.IndexTrans - 2] = tempHrf1
                            self.HasilTrans[self.IndexTrans - 3] = 'e'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        # 1015
                        else:
                            if (teks[x - 2] == ' ' and (teks[x - 3] != 'ī' or teks[x - 3] != 'ê' or teks[x - 3] != 'ú' or teks[x - 3] != 'ô' or teks[x - 3] != 'ā' or teks[x - 3] != 'â' or teks[x - 3] != 'ã' or teks[x - 3] != 'ä' or teks[x - 3] != 'ì' or teks[x - 3] != 'µ' or teks[x - 3] != 'a' or teks[x - 3] != 'i' or teks[x - 3] != 'u' or teks[x - 3] != 'e' or teks[x - 3] != 'o' or teks[x - 3] != 'é' or teks[x - 1] != 'h' or teks[x - 3] != 'r' or self.cecek == 0)):
                                tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                                self.HasilTrans[self.IndexTrans - 3] = 'e'
                                self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0
                            else:
                                tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                                self.HasilTrans[self.IndexTrans - 2] = 'e'
                                self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                                self.HasilTrans[self.IndexTrans] = tempHrf1
                                self.IndexTrans = self.IndexTrans + 1
                                self.gantungan = 0
                                self.cecek = 0
                        # end gantungan 1044
                    elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'eh'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans - 1] = 'e'
                        self.HasilTrans[self.IndexTrans] = tempHrf1
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case e ===***===           
        
        # ===***=== case é ===***=== 
        elif karakter == 'é':
            if x == 0:
                if (teks[x + 1] == 'n' and teks[x + 2] == 'g'):
                    self.HasilTrans[self.IndexTrans] = 'h'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'r':
                    self.HasilTrans[self.IndexTrans] = 'h'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = 'h)'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        if (teks[x + 1] == 'n' and teks[x + 2] == 'g'):
                            self.HasilTrans[self.IndexTrans] = 'h'
                            self.IndexTrans = self.IndexTrans + 1   
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'h)'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    #1122
                    elif (teks[x -2] == '.' or teks[x -2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'h)'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == 'n' and teks[x - 3] == 'g'):
                        self.HasilTrans[self.IndexTrans] = 'h)'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'À)'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                #1162
                elif teks[x + 1] == 'r':
                    if ((teks[x + 2] == 'ī') or (teks[x + 2] == 'ê') or (teks[x + 2] == 'ú') or (teks[x + 2] == 'ô') or (teks[x + 2] == 'ā') or (teks[x + 2] == 'â') or (teks[x + 2] == 'ã') or (teks[x + 2] == 'ä') or (teks[x + 2] == 'ì') or (teks[x + 2] == 'µ') or (teks[x + 2] == 'a') or (teks[x + 2] == 'u') or (teks[x + 2] == 'e') or (teks[x + 2] == 'o') or (teks[x + 2] == 'é') or (teks[x + 2] == 'i')):
                        self.HasilTrans[self.IndexTrans] = ')'
                        self.IndexTrans = self.IndexTrans + 1   
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = ''
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'h)'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x + 1] == 'n' and teks[x + 2] == 'g' and (teks[x + 3] == ' ' or teks[x + 3] == '.' or teks[x + 3] == ',')):
                    self.HasilTrans[self.IndexTrans] = ''
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = ')'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        # ===***=== end case é ===***=== 

        # ===***=== case g ===***=== 
        elif karakter == 'g':
            if x == 0:
                if teks[x + 1] == 'e':
                    self.HasilTrans[self.IndexTrans] = 'eg'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'G'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                elif teks[x + 1] == 'o':
                    self.HasilTrans[self.IndexTrans] = 'ego'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'g'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            # 1249
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'G'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'g'  
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    
                    elif teks[x - 2] == 'r':
                        if (self.gantungan == 1 or teks[x + 1] == 'ÿ'):
                            self.HasilTrans[x] = 'G'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'g'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'á'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                    # 1303
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'G'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'g'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecel = 0
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/G'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'á'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/g'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 1353
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'G'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'g'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                
                # 1375
                elif (teks[x + 1] == 'ÿ' and teks[x - 1] == 'r'):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'G'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'g'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                # 1403
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'G'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'g'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                # 1424
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/G'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/g'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case g ===***=== 

        # ===***=== case h ===***=== 
        elif karakter == 'h':
            if x == 0:
                self.HasilTrans[self.IndexTrans] = 'h'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if  (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'h'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'h'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'À'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or teks[x - 1] == 'r' or self.cecek == 1):

                    if (x == len(self.HasilTrans) - 1 or teks[x + 1] == ' ' or teks[x + 1] == '.' or teks[x +1] == ','):
                        self.HasilTrans[self.IndexTrans] = ';'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é'):
                        self.HasilTrans[self.IndexTrans] = 'h'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = ';'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                #1526
                elif (teks[x + 1] == 'a'):
                    self.HasilTrans[self.IndexTrans] = ''
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'h'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'À'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
        # ===***=== end case h ===***=== 

        # ===***=== case i ===***=== 
        elif karakter == 'i':
            if x == 0:
                if (teks[x + 1] == 'n' and teks[x + 2] == 'g'):
                    self.HasilTrans[self.IndexTrans] = 'h'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'hi'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if (teks[x + 1] == 'n' and teks[x + 2] == 'g'):
                            self.HasilTrans[self.IndexTrans] = 'h'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'hi'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'hi'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    elif (teks[x + 1] == 'n' and teks[x + 2] == 'g' and (teks[x + 3] == ' ' or teks[x + 3] == '.' or teks[x + 3] == ',')):
                        self.HasilTrans[self.IndexTrans] = ''
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ài'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                # 1631
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'hi'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x + 1] == 'a'):
                    self.HasilTrans[self.IndexTrans] = 'ê'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'hi'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x + 1] == 'n' and teks[x + 2] == 'g' and (teks[x + 3] == ' ' or teks[x + 3] == '.' or teks[x + 3] == ',')):
                    self.HasilTrans[self.IndexTrans] = ''
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'I'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'i'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        # ===***=== end case:i ===***=== 

        # ===***=== case j ===***=== 
        elif karakter == 'j':
            if x == 0:
                self.HasilTrans[self.IndexTrans] = 'j'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'j'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'j'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'é'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                    elif (teks[x - 2] == '.' or teks[x - 2] == ','):
                        self.HasilTrans[self.IndexTrans] = 'j'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'é'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/j'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'j'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0  
                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'j'
                        self.IndexTrans = self.IndexTrans + 1   
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'é'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                
                elif (teks[x - 1] == '.' or teks[x - 1] == ','):
                    self.HasilTrans[self.IndexTrans] = 'j'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'é'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/j'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case j ===***=== 

        # ===***=== case k ===***=== 
        elif karakter == 'k':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'K'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'K'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if (teks[x - 1] == ' ' or teks[x - 1] =='-'):
                    if ((teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (self.cecek == 1)):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'K'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'k'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/k'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'k'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ð'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'k'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Ð'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ð'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 1924
                elif (teks[x - 1] == ' ' or teks[x - 1] =='-'):
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == ' ':
                            self.HasilTrans[x] = 'K'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'K'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/K'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    elif teks[x - 1] == 'r':
                        if self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'k'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ð'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                    elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'j'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Ð'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/k'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                elif ((teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'i') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (teks[x - 1] == 'h') or (self.cecek == 1)):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'K'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'k'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/K'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'k'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ð'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'j'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    if ((x != len(self.HasilTrans) - 1) and ((teks[x + 1] == 'ī') or (teks[x + 1] == 'ê') or (teks[x + 1] == 'ú') or (teks[x + 1] == 'ô') or (teks[x + 1] == 'ā') or (teks[x + 1] == 'â') or (teks[x + 1] == 'ã') or (teks[x + 1] == 'ä') or (teks[x + 1] == 'ì') or (teks[x + 1] == 'µ') or (teks[x + 1] == 'a') or (teks[x + 1] == 'i') or (teks[x + 1] == 'u') or (teks[x + 1] == 'e') or (teks[x + 1] == 'o') or (teks[x + 1] == 'é') or (teks[x + 1] == 'r'))):
                        self.HasilTrans[self.IndexTrans] = 'Ð'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/k'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0                
        # ===***=== end case k ===***=== 

        # ===***=== case l ===***=== 
        elif karakter == 'l':
            if x == 0:
                if teks[x + 1] == 'é':
                    self.HasilTrans[self.IndexTrans] = 'ò'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'L'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'l'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'é':
                            self.HasilTrans[self.IndexTrans] = 'ò'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
                        elif teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'L'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'l'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    # 2070
                    elif teks[x - 2] == 'r':
                        if (self.gantungan == 1 and teks[x + 1] == 'ÿ'): 
                            self.HasilTrans[self.IndexTrans] = 'L'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'l'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Þ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'L'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'l'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif (teks[x + 1] == 'ÿ'):
                        self.HasilTrans[x] = '/L'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Þ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/l'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 2148
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'é':
                        self.HasilTrans[self.IndexTrans] = 'ò'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'L'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'l'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x - 1] == 'r':
                    if (self.gantungan == 1 and teks[x + 1] == 'ÿ'):
                        self.HasilTrans[self.IndexTrans] = 'L'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'L'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Þ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = 'L'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'l'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/L'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or  teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'Þ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/l'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case l ===***=== 

        # ===***=== case m ===***=== 
        elif karakter == 'm':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'M'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'm'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'M'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'm'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1 and teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'M'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1

                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'm'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                        else:
                            self.HasilTrans[self.IndexTrans] = 'ß'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0

                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):

                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'M'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1

                        else:
                            self.HasilTrans[self.IndexTrans] = 'm'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/M'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    else:
                        if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'ß'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/m'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'M'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'm'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                # 2411
                elif teks[x - 1] == 'r':
                    if (self.gantungan == 1 and teks[x + 1] == 'ÿ'):
                        self.HasilTrans[x] = 'M'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'm'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'ß'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'M'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'm'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/M'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if (x != len(self.HasilTrans) - 1 and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'ß'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/m'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case m ===***=== 

        # ===***=== case n ===***=== 
        elif karakter == 'n':
            if x == 0:
                if teks[x + 1] == 'g':
                    self.HasilTrans[self.IndexTrans] = '\\'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'y':
                    self.HasilTrans[self.IndexTrans] = 'z'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'N'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'n'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                self.gantungan = 0
            
            #2530
            elif teks[x - 1] == ' ':
                if teks[x + 1] == 'g':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):

                        if (teks[x + 2] == 'ī' or teks[x + 2] == 'ê' or teks[x + 2] == 'ú' or teks[x + 2] == 'ô' or teks[x + 2] == 'ā' or teks[x + 2] == 'â' or teks[x + 2] == 'ã' or teks[x + 2] == 'ä' or teks[x + 2] == 'ì' or teks[x + 2] == 'µ' or teks[x + 2] == 'a' or teks[x + 2] == 'i' or teks[x + 2] == 'u' or teks[x + 2] == 'e' or teks[x + 2] == 'o' or teks[x + 2] == 'é'):
                            self.HasilTrans[self.IndexTrans] = '\\'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
                        elif teks[x + 2] == ' ':
                            self.HasilTrans[self.IndexTrans] = '\\'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '*'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 1
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = '\\'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0  
                        self.cecek = 0
                    else:
                        if (teks[x + 2] == 'ī' or teks[x + 2] == 'ê' or teks[x + 2] == 'ú' or teks[x + 2] == 'ô' or teks[x + 2] == 'ā' or teks[x + 2] == 'â' or teks[x + 2] == 'ã' or teks[x + 2] == 'ä' or teks[x + 2] == 'ì' or teks[x + 2] == 'µ' or teks[x + 2] == 'a' or teks[x + 2] == 'i' or teks[x + 2] == 'u' or teks[x + 2] == 'e' or teks[x + 2] == 'o' or teks[x + 2] == 'é'):
                            self.HasilTrans[self.IndexTrans] = 'å'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '*'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 1
                
                # 2587
                elif teks[x + 1] == 'y':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'z'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == '.' or teks[x - 2] == ','):
                        self.HasilTrans[self.IndexTrans] = 'z'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'ñ'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 1
                        self.cecek = 0

                elif teks[x + 1] == 'j':
                    self.HasilTrans[self.IndexTrans] = 'zé'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        self.HasilTrans[x] = 'N'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/N'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                # 2644
                elif teks[x + 1] == 'c':
                    self.HasilTrans[self.IndexTrans] = 'zÇ'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                
                elif (x != len(self.HasilTrans) - 1 and teks[x - 2] == 'r' and teks[x - 3] == 'r'):
                    self.HasilTrans[self.IndexTrans] = 'x'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0  
                else:
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'N'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'n'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    #2683
                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'n'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/N'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    else:
                        if (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r'):
                            self.HasilTrans[self.IndexTrans] = 'Â'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/n'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0

            # 2732
            else:
                if teks[x + 1] == 'g':
                    if (teks[x + 2] == ' ' or teks[x + 2] == '.' or teks[x + 2] == ',' or teks[x + 2] == '?' or teks[x + 2] == '!'):
                        if teks[x - 1] == 'i':
                            self.HasilTrans[self.IndexTrans] = '&'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 1
                        elif teks[x - 1] == 'é':
                            self.HasilTrans[self.IndexTrans] = '%'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = '*'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 1  
                    
                    # 2766
                    elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or teks[x - 1] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = '\\'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                        self.HasilTrans[self.IndexTrans] = '\\'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'å'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 1
                        self.cecek = 0

                #  2792
                elif teks[x + 1] == 'j':
                    self.HasilTrans[self.IndexTrans] = 'zé'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'N'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1

                elif teks[x + 1] == 'y':
                    if (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or teks[x - 1] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'z'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0

                    elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'z'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'ñ'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 1
                        self.cecek = 0
                
                # 2838
                elif teks[x + 1] == 'c':
                    self.HasilTrans[self.IndexTrans] = 'zÇ'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                
                elif (x != len(self.HasilTrans) - 1 and teks[x - 1] == 'r' and teks[x - 2] == 'r'):
                    self.HasilTrans[self.IndexTrans] = 'x'
                    self.IndexTrans = self.IndexTrans + 1
                    self.Gantungan = 0
                    self.cecek = 0

                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'n'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/N'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or teks[x - 1] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'n'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'Â'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/n'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
        # ===***=== end case n ===***=== 

        # ===***=== case o ===***=== 
        elif karakter == 'o':
            if x == 0:
                if (teks[x + 1] == 'm' and teks[x + 2] == ' '):
                    self.HasilTrans[self.IndexTrans] = 'þ'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                elif (teks[x + 1] == 'n' and teks[x + 2] == 'g' and teks[x + 3] == ' '):
                    self.HasilTrans[self.IndexTrans] = 'þ'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'eho'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            
            #3190
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'h' and teks[x + 1] == 'm'):
                        self.HasilTrans[self.IndexTrans] = 'þ'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0  
                        self.katakhusus = 1
                    elif (teks[x + 1] == 'm' and teks[x + 2] == ' '):
                        self.HasilTrans[self.IndexTrans] = 'þ'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    # 3215
                    elif (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i' or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'eho'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    elif (teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':'):
                        self.HasilTrans[self.IndexTrans] = 'eho'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        tempHrf1 = self.HasilTrans[self.IndexTrans - 2]
                        if self.gantungan == 1:
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            self.HasilTrans[self.IndexTrans - 2] = 'e'
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.HasilTrans[self.IndexTrans] = tempHrf1 +'o'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans - 1] = 'e'
                            self.HasilTrans[self.IndexTrans] = tempHrf1 +'o'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 3263
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'eho'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':'):
                    self.HasilTrans[self.IndexTrans] = 'eho'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif teks[x - 1] == 'ÿ':
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 1]
                    self.HasilTrans[self.IndexTrans] = tempHrf2
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0  

                elif (self.gantungan == 0 and teks[x - 1] == 'g' and teks[x - 2] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                #3309
                elif (self.gantungan == 0 and teks[x - 1] == 'y' and teks[x - 2] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    self.HasilTrans[self.IndexTrans - 2] = 'e'
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (self.gantungan == 1 and teks[x - 2] == 'g' and teks[x - 3] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                    self.HasilTrans[self.IndexTrans - 3] = 'e'
                    self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (self.gantungan == 1 and teks[x - 2] == 'y' and teks[x - 3] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                    self.HasilTrans[self.IndexTrans - 3] = 'e'
                    self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (self.gantungan == 1 and teks[x - 1] == 'g' and teks[x - 2] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                    self.HasilTrans[self.IndexTrans - 3] = 'e'  
                    self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (self.gantungan == 1 and teks[x - 1] == 'y' and teks[x - 2] == 'n'):
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                    tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                    tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                    self.HasilTrans[self.IndexTrans - 3] = 'e'
                    self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                    self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                    self.HasilTrans[self.IndexTrans] = 'o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                else:
                    tempHrf1 = self.HasilTrans[self.IndexTrans - 1]

                    if self.gantungan == 1:
                        if (teks[x - 2] == ' ' and (teks[x - 3] != 'ī' or teks[x - 3] != 'ê' or teks[x - 3] != 'ú' or teks[x - 3] != 'ô' or teks[x - 3] != 'ā' or teks[x - 3] != 'â' or teks[x - 3] != 'ã' or teks[x - 3] != 'ä' or teks[x - 3] != 'ì' or teks[x - 3] != 'µ' or teks[x - 3] != 'a' or teks[x - 3] != 'i'  or teks[x - 3] != 'u' or teks[x - 3] != 'e' or teks[x - 3] != 'o' or teks[x - 3] != 'é' or teks[x - 3] != 'h' or teks[x - 3] != 'r' or self.cecek == 0)):
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            tempHrf3 = self.HasilTrans[self.IndexTrans - 3]
                            self.HasilTrans[self.IndexTrans - 3] = 'e'
                            self.HasilTrans[self.IndexTrans - 2] = tempHrf3
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf1
                            self.HasilTrans[self.IndexTrans] = 'o'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            tempHrf2 = self.HasilTrans[self.IndexTrans - 2]
                            self.HasilTrans[self.IndexTrans - 2] = 'e'
                            self.HasilTrans[self.IndexTrans - 1] = tempHrf2
                            self.HasilTrans[self.IndexTrans] = tempHrf1 + 'o'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    else:
                        self.HasilTrans[self.IndexTrans - 1] = 'e'
                        self.HasilTrans[self.IndexTrans] = tempHrf1 + 'o'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case o ===***=== 

        # ===***=== case p ===***=== 
        elif karakter == 'p':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'P'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'p'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'P'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'p'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    
                    # 3483
                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1 and teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'P'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1 
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'p'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'æ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0 
                    #3513
                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'P'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'p'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        
                    # 3533
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/P'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                            self.HasilTrans[self.IndexTrans] = 'æ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        
                        elif teks[x + 1] == 'w':
                            self.HasilTrans[self.IndexTrans] = 'æ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/p'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 3572
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'A'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'p'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                # 3594
                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'P'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'p'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'æ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                # 3625
                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'P'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'p'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/P'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    #3655
                    if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')):
                        self.HasilTrans[self.IndexTrans] = 'æ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                    elif teks[x + 1] == 'w':
                        self.HasilTrans[self.IndexTrans] = 'æ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/p'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case p ===***=== 

        # ===***=== case r ===***=== 
        elif karakter == 'r':
            if x == 0:
                if teks[x + 1] == 'é':
                    self.HasilTrans[self.IndexTrans] = 'Ï'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'R'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'r'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        if teks[x + 1] == 'é':
                            self.HasilTrans[self.IndexTrans] = 'Ï'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
                        elif teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'R'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'r'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    
                    # 3747
                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'R'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'r'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    
                    # 3767
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = '/R'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        if teks[x + 1] == 'é':
                            self.HasilTrans[self.IndexTrans] = 'Ï'
                            self.IndexTrans = self.IndexTrans + 2
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'É'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                # 3804
                elif teks[x - 1] == 'â':
                    self.HasilTrans[self.IndexTrans] = 'r'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1): 

                    if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é')): 
                        self.HasilTrans[self.IndexTrans] = 'r'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x + 1] == 'é':
                        self.HasilTrans[self.IndexTrans] = 'Ï'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[self.IndexTrans] = 'R'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        if teks[x - 1] == 'o':
                            tempHrf1 = self.HasilTrans[self.IndexTrans - 1]
                            self.HasilTrans[self.IndexTrans] = tempHrf1
                            self.HasilTrans[self.IndexTrans - 1] = '('
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        elif teks[x - 1] == 'é':
                            self.HasilTrans[self.IndexTrans] = '$'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '('
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                # 3867
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[self.IndexTrans] = 'R'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if teks[x + 1] == 'é' and (teks[x - 1] == '.' or teks[x - 1] == ','):
                        self.HasilTrans[self.IndexTrans] = 'Ï'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    elif  teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                        self.HasilTrans[self.IndexTrans] = 'r'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0  
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'É'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
        # ===***=== end case r ===***===  

        # ===***=== case s ===***=== 
        elif karakter == 's':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'S'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 's'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            
            elif (x != len(self.HasilTrans) - 1):
                if teks[x - 1] == ' ':
                    if teks[x - 2] == 'h' and teks[x - 3] == 'i':
                        self.HasilTrans[self.IndexTrans] = ']'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1

                    elif (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'S'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 's'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    # 3967
                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1 and teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'S'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 's'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'uæ'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0

                    # 3994
                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'S'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 's'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    # 4015
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/S'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    elif teks[x - 2] == 'm' and self.katakhusus == 1:
                        if teks[x + 2] == 'n':
                            self.HasilTrans[self.IndexTrans] = ']'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 's'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'uæ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                # 4072
                elif teks[x + 1] == 'c':
                    self.HasilTrans[self.IndexTrans] = '['
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                elif teks[x + 1] == 's':
                    self.HasilTrans[self.IndexTrans] = ']Ö'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                elif teks[x + 1] == 's':
                    self.HasilTrans[self.IndexTrans] = ']Ö'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 1
                    self.cecek = 0
                
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'S'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 's'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                # 4118
                elif teks[x - 1] == 'r':
                    if self.gantungan == 1 and teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'S'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 's'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'uæ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                
                #4144
                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'S'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 's'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/S'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'uæ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
        # ===***=== end case s ===***=== 

        # ===***=== case t ===***=== 
        elif karakter == 't':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'T'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 't'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'T'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 't'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x - 2] == 'r':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'T'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 't'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ó'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                    
                    #4623
                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[self.IndexTrans] = 'T'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 't'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/T'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    
                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é') and (teks[x + 1] == 'r')): 
                            self.HasilTrans[self.IndexTrans] = 'Ó'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0

                        elif (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r' or self.cecek == 1):
                            self.HasilTrans[self.IndexTrans] = 'Ó'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/t'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                # 4326
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or teks[x - 1] == 'h' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'T'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 't'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif teks[x - 1] == 'r':
                    if self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 't'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ó'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                # 4366
                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'T'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 't'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'T'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if ((x != len(self.HasilTrans) - 1) and ((teks[x + 1] == 'ī') or (teks[x + 1] == 'ê') or (teks[x + 1] == 'ú') or (teks[x + 1] == 'ô') or (teks[x + 1] == 'a') or (teks[x + 1] == 'i') or (teks[x + 1] == 'u') or (teks[x + 1] == 'e') or (teks[x + 1] == 'o') or (teks[x + 1] == 'é') or (teks[x + 1] == 'r'))):
                        self.HasilTrans[self.IndexTrans] = 'Ó'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/t'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case t ===***=== 

        # ===***=== case u ===***===  
        elif karakter == 'u':
            if x == 0:
                self.HasilTrans[self.IndexTrans] = 'hu'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0

            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or teks[x - 2] == 'r' or self.cecek == 1):
                        self.HasilTrans[self.IndexTrans] = 'hu'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        self.HasilTrans[self.IndexTrans] = 'hu'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'À¡'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    self.HasilTrans[self.IndexTrans] = 'hu'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

                #4469 
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i' or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    self.HasilTrans[self.IndexTrans] = 'hu'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                
                #4477
                elif x != len(self.HasilTrans) - 1 and teks[x + 1] == 'a':
                    if (teks[x - 1] != 'ī' or teks[x - 1] != 'ê' or teks[x - 1] != 'ú' or teks[x - 1] != 'ô' or teks[x - 1] != 'ā' or teks[x - 1] != 'â' or teks[x - 1] != 'ã' or teks[x - 1] != 'ä' or teks[x - 1] != 'ì' or teks[x - 1] != 'µ' or teks[x - 1] != 'a' or teks[x - 1] != 'i' or teks[x - 1] != 'u' or teks[x - 1] != 'e' or teks[x - 1] != 'o' or teks[x - 1] != 'é'):
                        self.HasilTrans[self.IndexTrans] = 'Ù'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'wu'
                        self.IndexTrans = self.IndexTrans + 2
                        self.gantungan = 0
                        self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'u'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
        # ===***=== end case u ===***=== 

        # ===***=== case w ===***===
        elif karakter == 'w':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'W'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[self.IndexTrans] = 'w'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
            
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'W'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'w'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    # 4561
                    elif teks[x - 2] == 'r':
                        if self.gantungan == 1 and teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'W'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        elif self.gantungan == 1:
                            self.HasilTrans[self.IndexTrans] = 'w'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = 'Ù'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                    # 4589
                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'W'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'w'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0

                    # 4610
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = '/W'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')): 
                            self.HasilTrans[self.IndexTrans] = 'Ù'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/w'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                # 4639
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'W'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'w'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                
                elif self.gantungan == 1 and teks[x - 1] == 'r':
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'W'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    elif self.gantungan == 1:
                        self.HasilTrans[self.IndexTrans] = 'w'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = 'Ù'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                
                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'W'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'w'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0

                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = '/W'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1

                else:
                    if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')): 
                        self.HasilTrans[self.IndexTrans] = 'Ù'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    else:
                        self.HasilTrans[self.IndexTrans] = '/w'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # ===***=== end case w ===***=== 

        # ===***=== case y ===***=== 
        elif karakter == 'y':
            if x == 0:
                if teks[x + 1] == 'e':
                    self.HasilTrans[self.IndexTrans] = 'ey'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'Y'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                elif teks[x + 1] == 'o':
                    self.HasilTrans[self.IndexTrans] = 'eyo'
                    self.IndexTrans = self.IndexTrans + 2
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'y'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0

            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī' or teks[x - 2] == 'ê' or teks[x - 2] == 'ú' or teks[x - 2] == 'ô' or teks[x - 2] == 'ā' or teks[x - 2] == 'â' or teks[x - 2] == 'ã' or teks[x - 2] == 'ä' or teks[x - 2] == 'ì' or teks[x - 2] == 'µ' or teks[x - 2] == 'a' or teks[x - 2] == 'i'  or teks[x - 2] == 'u' or teks[x - 2] == 'e' or teks[x - 2] == 'o' or teks[x - 2] == 'é' or teks[x - 2] == 'h' or self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'Y'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[self.IndexTrans] = 'y'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'Y'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1

                    elif teks[x - 2] == '.' or teks[x - 2] == ',' or teks[x - 2] == ':':
                        self.HasilTrans[self.IndexTrans] = 'y'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    # 4828
                    else:
                        if ((x != len(self.HasilTrans) - 1) and (teks[x + 1] == 'ī' or teks[x + 1] == 'ê' or teks[x + 1] == 'ú' or teks[x + 1] == 'ô' or teks[x + 1] == 'ā' or teks[x + 1] == 'â' or teks[x + 1] == 'ã' or teks[x + 1] == 'ä' or teks[x + 1] == 'ì' or teks[x + 1] == 'µ' or teks[x + 1] == 'a' or teks[x + 1] == 'i' or teks[x + 1] == 'u' or teks[x + 1] == 'e' or teks[x + 1] == 'o' or teks[x + 1] == 'é' or teks[x + 1] == 'r')): 
                            self.HasilTrans[self.IndexTrans] = 'ê'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                        else:
                            self.HasilTrans[self.IndexTrans] = '/y'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                # 4847
                elif (teks[x - 1] == 'ī' or teks[x - 1] == 'ê' or teks[x - 1] == 'ú' or teks[x - 1] == 'ô' or teks[x - 1] == 'ā' or teks[x - 1] == 'â' or teks[x - 1] == 'ã' or teks[x - 1] == 'ä' or teks[x - 1] == 'ì' or teks[x - 1] == 'µ' or teks[x - 1] == 'a' or teks[x - 1] == 'i'  or teks[x - 1] == 'u' or teks[x - 1] == 'e' or teks[x - 1] == 'o' or teks[x - 1] == 'é' or self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'Y'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[self.IndexTrans] = 'y'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'Y'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                
                elif teks[x - 1] == '.' or teks[x - 1] == ',' or teks[x - 1] == ':':
                    self.HasilTrans[self.IndexTrans] = 'y'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[self.IndexTrans] = 'ê'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
        # ===***=== end case y ===***=== 

        # case tanda baca
        elif karakter == ' ':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ''
        elif karakter == ':':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ':'
        elif karakter == '-':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ''
        elif karakter == ';':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ':'
        elif karakter == '"':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ':'
        elif karakter == '“':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ':'
        elif karakter == '”':
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = ':'
        
        elif karakter == '.':
            if x == 0:
                self.HasilTrans[x] == '.'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                if (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'i') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (teks[x - 1] == 'h') or (teks[x - 1] == ':'):
                    self.HasilTrans[x] = '.'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == '1') or (teks[x - 1] == '2') or (teks[x - 1] == '3') or (teks[x - 1] == '4') or (teks[x - 1] == '5') or (teks[x - 1] == '6') or (teks[x - 1] == '7') or (teks[x - 1] == '8') or (teks[x - 1] == '9') or (teks[x - 1] == '0'):
                    self.HasilTrans[x] = '.'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x - 1] == 'þ' or teks[x - 1] == '°':
                    self.HasilTrans[x] = '.'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                elif teks[x - 1] == '.':
                    self.HasilTrans[x] = '.'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    if (teks[x - 1] == 'r') and (self.gantungan == 1):
                        self.HasilTrans[x] = '.'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 1] == 'g') and (teks[x - 2] == 'n'):
                        self.HasilTrans[x] = '.'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x - 1] == 'm' and self.katakhusus == 1:
                        self.HasilTrans[x] = '.'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif teks[x - 1] == '>':
                        self.HasilTrans[x] = '.'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/.'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        elif karakter == ',':
            if x == 0:
                self.HasilTrans[x] == ','
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                if (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'i') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (teks[x - 1] == 'h') or (teks[x - 1] == ':'):
                    self.HasilTrans[x] = ','
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif (teks[x - 1] == '1') or (teks[x - 1] == '2') or (teks[x - 1] == '3') or (teks[x - 1] == '4') or (teks[x - 1] == '5') or (teks[x - 1] == '6') or (teks[x - 1] == '7') or (teks[x - 1] == '8') or (teks[x - 1] == '9') or (teks[x - 1] == '0'):
                    self.HasilTrans[x] = ','
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    if (teks[x - 1] == 'r') and (self.gantungan == 1):
                        self.HasilTrans[x] = ','
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 1] == 'g') and (teks[x - 2] == 'n'):
                        self.HasilTrans[x] = ','
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 1] == 'm' and self.katakhusus == 1):
                        self.HasilTrans[x] = ','
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/,'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
        # end case tanda baca "

        #case angka
        elif karakter == '1':
            if x == 0:
                self.HasilTrans[x] = '1'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '1'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '2':
            if x == 0:
                self.HasilTrans[x] = '2'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '2'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '3':
            if x == 0:
                self.HasilTrans[x] = '3'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '3'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '4':
            if x == 0:
                self.HasilTrans[x] = '4'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '4'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '5':
            if x == 0:
                self.HasilTrans[x] = '5'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '5'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '6':
            if x == 0:
                self.HasilTrans[x] = '6'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '6'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '7':
            if x == 0:
                self.HasilTrans[x] = '7'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '7'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '8':
            if x == 0:
                self.HasilTrans[x] = '8'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '8'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '9':
            if x == 0:
                self.HasilTrans[x] = '9'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '9'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == '0':
            if x == 0:
                self.HasilTrans[x] = '0'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
            else:
                self.HasilTrans[x] = '0'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        #end case angka

        # case karakter khusus
        elif karakter == 'ā':
            if x == 0:
                self.HasilTrans[x] = 'õ'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == 'þ' or teks[x - 2] == '°'):
                        self.HasilTrans[x] = 'õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                    
                # 5347
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                elif teks[x - 1] == 'þ' or teks[x - 1] == '°':
                    self.HasilTrans[x] = 'õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ӑ':
            if x == 0:
                self.HasilTrans[x] = 'Á'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'Á'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = 'Á'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ī':
            if x == 0:
                self.HasilTrans[x] = '÷o'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '÷o'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '÷o'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/÷o'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0

                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '÷o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/÷o'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ú':
            if x == 0:
                self.HasilTrans[x] = 'úo'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'úo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'úo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/úo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'úo'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/úo'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ê':
            if x == 0:
                self.HasilTrans[x] = 'ü'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'ü'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'ü'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/ü'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'ü'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/ü'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ô':
            if x == 0:
                self.HasilTrans[x] = 'Oo'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'Oo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'Oo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/Oo'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'Oo'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/Oo'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ṭ':
            if x == 0:
                self.HasilTrans[x] = '`'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '`'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '`'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/`'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif  (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '`'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/`'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ś':
            if x == 0:
                self.HasilTrans[x] = ']'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = ']'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = ']'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/]'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = ']'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/]'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'š':
            if x == 0:
                self.HasilTrans[x] = '['
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '['
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '/['
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ṣ':
            if x == 0:
                self.HasilTrans[x] = '['
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/['
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '['
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '['
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'ṛ':
            if x == 0:
                self.HasilTrans[x] = 'Ï'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                self.HasilTrans[x] = 'Ï'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == 'ṛ':
            if x == 0:
                self.HasilTrans[x] = 'Ï'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                self.HasilTrans[x] = 'Ï'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 0
                self.cecek = 0
        elif karakter == 'þ':
            if x == 0:
                self.HasilTrans[x] = 'þ'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'þ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'þ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = 'þ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'þ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = 'þ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == '°':
            if x == 0:
                self.HasilTrans[x] = '>'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '>'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '>'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '>'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '>'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = '>'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'â':
            if x == 0:
                self.HasilTrans[x] = 'Á'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = '/Á'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'Á'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = 'Á'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == 'î':
            self.HasilTrans[x] = 'Õ'
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
            self.katakhusus = 1
        elif karakter == 'ï':
            self.HasilTrans[x] = 'Õ'
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
            self.katakhusus = 1
        elif karakter == 'ä':
            if x == 0:
                self.HasilTrans[x] = 'a'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'a'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'a'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                    else:
                        self.HasilTrans[x] = 'Õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'a'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                else:
                    self.HasilTrans[x] = 'Õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
        elif karakter == '|':
            if x == 0:
                self.HasilTrans[x] = '|'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '|'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = '|'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/|'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '|'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/|'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == '}':
            if x == 0:
                self.HasilTrans[x] = '}'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = '}'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans = '}'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/}'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = '}'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/}'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == 'ã':
            if x == 0:
                self.HasilTrans[x] = 'õ'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans = 'õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/õ'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/õ'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == 'ñ':
            if x == 0:
                self.HasilTrans[x] = 'x'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'x'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans = 'x'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/x'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'x'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/x'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == 'ì':
            if x == 0:
                self.HasilTrans[x] = 'hI'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if  teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'hI'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'hI'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = 'I'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'hI'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'I'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == 'µ':
            if x == 0:
                self.HasilTrans[x] = 'hU'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = 'hU'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'hU'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = 'U'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = 'hU'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'U'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == 'æ':
            if x == 0:
                if teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'F'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'f'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        if teks[x + 1] == 'ÿ':
                            self.HasilTrans[x] = 'F'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 1
                            self.cecek = 0
                            self.katakhusus = 1
                        else:
                            self.HasilTrans[x] = 'f'
                            self.IndexTrans = self.IndexTrans + 1
                            self.gantungan = 0
                            self.cecek = 0
                            self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = 'f'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'F'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = 'â'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    if teks[x + 1] == 'ÿ':
                        self.HasilTrans[x] = 'F'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = 'f'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                elif teks[x + 1] == 'ÿ':
                    self.HasilTrans[x] = 'F'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 1
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = 'â'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        elif karakter == ']':
            if x == 0:
                self.HasilTrans[x] = ']'
                self.IndexTrans = self.IndexTrans + 1
                self.gantungan = 1
                self.cecek = 0
                self.katakhusus = 1
            else:
                if teks[x - 1] == ' ':
                    if (teks[x - 2] == 'ī') or (teks[x - 2] == 'ê') or (teks[x - 2] == 'ú') or (teks[x - 2] == 'ô') or (teks[x - 2] == 'ā') or (teks[x - 2] == 'â') or (teks[x - 2] == 'ã') or (teks[x - 2] == 'ä') or (teks[x - 2] == 'ì') or (teks[x - 2] == 'µ') or (teks[x - 2] == 'a') or (teks[x - 2] == 'i') or (teks[x - 2] == 'u') or (teks[x - 2] == 'e') or (teks[x - 2] == 'o') or (teks[x - 2] == 'é') or (teks[x - 2] == 'h') or (teks[x - 2] == 'r') or (self.cecek == 1):
                        self.HasilTrans[x] = ']'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    elif (teks[x - 2] == ',') or (teks[x - 2] == '.') or (teks[x - 2] == ':'):
                        self.HasilTrans[x] = ']'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 0
                        self.cecek = 0
                        self.katakhusus = 1
                    else:
                        self.HasilTrans[x] = '/]'
                        self.IndexTrans = self.IndexTrans + 1
                        self.gantungan = 1
                        self.cecek = 0
                        self.katakhusus = 1
                elif (teks[x - 1] == 'ī') or (teks[x - 1] == 'ê') or (teks[x - 1] == 'ú') or (teks[x - 1] == 'ô') or (teks[x - 1] == 'ā') or (teks[x - 1] == 'â') or (teks[x - 1] == 'ã') or (teks[x - 1] == 'ä') or (teks[x - 1] == 'ì') or (teks[x - 1] == 'µ') or (teks[x - 1] == 'a') or (teks[x - 1] == 'u') or (teks[x - 1] == 'e') or (teks[x - 1] == 'o') or (teks[x - 1] == 'é') or (self.cecek == 1):
                    self.HasilTrans[x] = ']'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
                else:
                    self.HasilTrans[x] = '/]'
                    self.IndexTrans = self.IndexTrans + 1
                    self.gantungan = 0
                    self.cecek = 0
                    self.katakhusus = 1
        # end case karakter khusus

        # case huruf tak terdefinisi pada aksara bali
        elif karakter == 'f':
            self.HasilTrans[x] == ''
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
        elif karakter == 'q':
            self.HasilTrans[x] == ''
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
        elif karakter == 'v':
            self.HasilTrans[x] == ''
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
        elif karakter == 'x':
            self.HasilTrans[x] == ''
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
        elif karakter == 'z':
            self.HasilTrans[x] == ''
            self.IndexTrans = self.IndexTrans + 1
            self.gantungan = 0
            self.cecek = 0
        # end case huruf tak terdefinisi pada aksara bali

        else:
            self.IndexTrans = self.IndexTrans + 1
            self.HasilTrans[x] = str(karakter)
            self.gantungan = 0
            self.cecek = 0
                    