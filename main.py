class Durak_game:
    def __init__(self, col_players):
        self.col_players = col_players


    def create_pack():
        masti = ('pika','trefa','bubna','chervi')
        nominali = ('6','7','8','9','10','valet','dama','korol','tuz')
        koloda = []
        for mast in masti:
            weight = 0
            for nom in nominali:
                koloda.append({'mast':mast,'nom':nom,'weight':weight})
                weight += 1
        return koloda

    def razdat_kolodu(self):
        import random
        koloda = Durak_game.create_pack()
        self.game_baza = []
        igrok = 'igrok'
        for i in range(self.col_players):
            name = igrok + str(i)
            pl_koloda = []
            for x in range(6):
                pl_koloda.append(koloda.pop(random.randint(0,len(koloda)-1)))
            self.game_baza.append({name:name,'koloda':pl_koloda})
            #game_baza.append(pl_koloda)
        self.game_baza.append({'game_baza':'game_baza','koloda':koloda})
        return self.game_baza

    def proverka_kolod_igroka(self):
        koloda = self.game_baza[self.nomer_otb_igroka]['koloda']
        karta = self.karta_zaprosa
        dostup_mast = []
        for i in range(len(koloda)):
            dostup_mast.append(koloda[i]['mast'])
        dostup_mast = set(dostup_mast)
        varianti = []
        if karta['mast'] in dostup_mast:
            for x in koloda:
                if karta['mast'] == x['mast']:
                    if karta['weight'] < x['weight']:
                        varianti.append(x)
            if len(varianti) > 0:
                self.varianti = {'varianti':len(varianti),'koloda':varianti}
            else:
                self.varianti = {'varianti': len(varianti), 'koloda': varianti}
        else:
            self.varianti = {'varianti':len(varianti),'koloda':varianti}
        return self.varianti

    #game_baza,nomer_act_igroka
    def hod_brosok(self):
        import random
        activ_player = self.game_baza[self.nomer_act_igroka]
        print("Ходит игрок: ", list(activ_player.keys())[0])
        if len(activ_player['koloda']) > 0:
            koloda = activ_player['koloda']
            self.karta_zaprosa = koloda.pop(random.randint(0,len(koloda)-1))
            print("Бросает карту масти ", self.karta_zaprosa['mast']," ", self.karta_zaprosa['nom'])
            self.game_baza[self.nomer_act_igroka] = {list(activ_player.keys())[0]:list(activ_player.keys())[0],'koloda':koloda}
        return self.game_baza

    #game_baza, nomer_otb_igroka
    def dobor_karti_igrokom(self):
        import random
        activ_plaer = self.game_baza[self.nomer_otb_igroka]
        if len(self.game_baza[-1]['koloda'])>0:
            osnovnaia_koloda = self.game_baza[-1]['koloda']
            karta_dobora = osnovnaia_koloda.pop(random.randint(0,len(osnovnaia_koloda)-1))
            koloda = activ_plaer['koloda']
            koloda.append(karta_dobora)
            self.game_baza[self.nomer_otb_igroka] = {list(activ_plaer.keys())[0]: list(activ_plaer.keys())[0],'koloda': koloda}
            print("Игрок ",list(activ_plaer.keys())[self.nomer_otb_igroka]," добирае из колоды карту : ",karta_dobora )
        return self.game_baza

    # получает список из вариантов ответного хода
    # возвращает карту или None
    def vibrat_karty(self):
        import random
        if self.varianti['varianti'] > 1:
            self.karta_otvet = self.varianti['koloda'][random.randint(0,len(self.varianti['koloda'])-1)]
        elif self.varianti['varianti'] == 1:
            self.karta_otvet = self.varianti['koloda'][0]
        else:
            self.karta_otvet = None
        if self.karta_otvet != None:
            print(list(self.game_baza[self.nomer_otb_igroka].keys())[0], ' в ответ идет ' , self.karta_otvet['mast'] , ' ' , self.karta_otvet['nom'])
        else:
            print(list(self.game_baza[self.nomer_otb_igroka].keys())[0]," берет карту из колоды")

        return self.karta_otvet

    # удаляет карту ответ из колоды игрока
    def ubrat_karty_izcolodi_igroka(self):
        (self.game_baza[self.nomer_otb_igroka]['koloda']).remove(self.karta_otvet)




game = Durak_game(2)

game.razdat_kolodu()
game.nomer_act_igroka = 0
game.nomer_otb_igroka = 1
game.hod_brosok()
game.proverka_kolod_igroka()
if game.varianti['varianti'] == 0:
    while game.varianti['varianti'] == 0 and len(game.game_baza[-1]['koloda']) > 0:
        game.dobor_karti_igrokom()
        game.proverka_kolod_igroka()
    game.vibrat_karty()
else:
    game.vibrat_karty()
if (game.varianti['varianti'] == 0 and len(game.game_baza[-1]['koloda']) == 0) !=True:
    game.ubrat_karty_izcolodi_igroka()
    game.nomer_act_igroka = 1
    game.nomer_otb_igroka = 0
    game.hod_brosok()
    game.proverka_kolod_igroka()
    if game.varianti['varianti'] == 0:
        while game.varianti['varianti'] == 0 and len(game.game_baza[-1]['koloda']) > 0:
            game.dobor_karti_igrokom()
            game.proverka_kolod_igroka()
        game.vibrat_karty()
    else:
        game.vibrat_karty()
    if (game.varianti['varianti'] == 0 and len(game.game_baza[-1]['koloda']) == 0) != True:
        game.ubrat_karty_izcolodi_igroka()
    else:
        print("Игрок", str(game.nomer_act_igroka), " выиграл")
else:
    print("Игрок",str(game.nomer_act_igroka)," выиграл")
