def reset(money, money_max, ennemies, bullets, vagues, emplacements, vie, vie_max, vague):
    money = money_max
    ennemies = []
    bullets = []
    
    for e in emplacements:
        e.reset()

    for v in vagues:
        v.reset()

    print(vie)
    vie = vie_max
    print(vie)
    vague = 0