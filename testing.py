def test(LEAGUE):
    print(f"League:")
    print("\nSupermax Players:")
    for player in LEAGUE.super:
        print(f"- {player.Player}")

    print("\nMax Contract Players:") 
    for player in LEAGUE.max:
        print(f"- {player.Player}")

    print("\nMinimum Contract Players:")
    for player in LEAGUE.min:
        print(f"- {player.Player}")

    print("\nTier 1 Players ($25M-$31.8M):")
    for player in LEAGUE.t1:
        print(f"- {player.Player}")

    print("\nTier 2 Players ($20M-$25M):")
    for player in LEAGUE.t2:
        print(f"- {player.Player}")

    print("\nTier 3 Players ($15M-$20M):")
    for player in LEAGUE.t3:
        print(f"- {player.Player}")

    print("\nTier 4 Players ($10M-$15M):")
    for player in LEAGUE.t4:
        print(f"- {player.Player}")

    print("\nTier 5 Players ($5M-$10M):")
    for player in LEAGUE.t5:
        print(f"- {player.Player}")

    print("\nTier 6 Players ($0-$5M):")
    for player in LEAGUE.t6:
        print(f"- {player.Player}")

    print("\nPoint Guards:")
    for player in LEAGUE.pg:
        print(f"- {player.Player}")

    print("\nShooting Guards:")
    for player in LEAGUE.sg:
        print(f"- {player.Player}")

    print("\nSmall Forwards:")
    for player in LEAGUE.sf:
        print(f"- {player.Player}")

    print("\nPower Forwards:")
    for player in LEAGUE.pf:
        print(f"- {player.Player}")

    print("\nCenters:")
    for player in LEAGUE.center:
        print(f"- {player.Player}")




