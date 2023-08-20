


def calculate_points(real_home_score, real_away_score, predicted_home_score, predicted_away_score):
    # 5 punktow gdy dokladny wynik trafiony
    # 2 punkty gdy rezultat trafiony
    # 0 punktow gdy nic nie trafione
    if real_home_score == predicted_home_score and real_away_score == predicted_away_score:
        return 5
    # 3:1 i 1:0, 1:3 i 0:3  a nie trafiony 1:3 i 1:0
    if real_home_score-real_away_score > 0 and predicted_home_score-predicted_away_score > 0:
        return 2
    if real_home_score-real_away_score == 0 and predicted_home_score-predicted_away_score == 0:
        return 2
    if real_home_score-real_away_score < 0 and predicted_home_score-predicted_away_score < 0:
        return 2