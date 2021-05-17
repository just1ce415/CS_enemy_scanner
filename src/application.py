from flask import Flask, render_template, request, url_for
from get_stats_module import start
from adt import RecomendationADT
from gevent.pywsgi import WSGIServer



app = Flask(__name__)


information_lst = []
add_info = []
counter = 1


@app.route("/")
def index():
    return render_template("1.html")

@app.route("/new", methods = ['POST'])
def register():
    global information_lst

    name = request.form.get('nickname_url')
    name = f"'{request.form.get('nickname_url')}'" 

    print(name)
    if "/" not in name[-3:]: 
        name = name[:-1] + "/'"

    print(name)

    player_info = start(name, "mirage")
    information_lst.append(player_info)
    if len(information_lst) == 1:
        return render_template("1.html",your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                        kd = information_lst[0][3], win_rate = information_lst[0][2], adr = information_lst[0][4],
                                        headshot = information_lst[0][8], accur = information_lst[0][7][0][0],
                                        accur2 = information_lst[0][7][1][0], accur3 = information_lst[0][7][2][0],
                                        weapon_img10 = f"{information_lst[0][7][0][1]}.png", weapon_img11 = f"{information_lst[0][7][1][1]}.png",
                                        weapon_img12 = f"{information_lst[0][7][2][1]}.png")

    if len(information_lst) == 2:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         kd = information_lst[0][3], win_rate = information_lst[0][2], adr = information_lst[0][4],
                                         headshot = information_lst[0][8], accur = information_lst[0][7][0][0],
                                         accur2 = information_lst[0][7][1][0], accur3 = information_lst[0][7][2][0],
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         kd2 = information_lst[1][3], win_rate2 = information_lst[1][2], adr2 = information_lst[1][4],
                                         headshot2 = information_lst[1][8], accur20 = information_lst[1][7][0][0],
                                         accur21 = information_lst[1][7][1][0], accur22 = information_lst[1][7][2][0],
                                         weapon_img10 = f"{information_lst[0][7][0][1]}.png", weapon_img11 = f"{information_lst[0][7][1][1]}.png",
                                         weapon_img12 = f"{information_lst[0][7][2][1]}.png", weapon_img20 = f"{information_lst[1][7][0][1]}.png",
                                         weapon_img21 = f"{information_lst[1][7][1][1]}.png", weapon_img22 = f"{information_lst[1][7][2][1]}.png")
    if len(information_lst) == 3:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         kd = information_lst[0][3], win_rate = information_lst[0][2], adr = information_lst[0][4],
                                         headshot = information_lst[0][8], accur = information_lst[0][7][0][0],
                                         accur2 = information_lst[0][7][1][0], accur3 = information_lst[0][7][2][0],
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         kd2 = information_lst[1][3], win_rate2 = information_lst[1][2], adr2 = information_lst[1][4],
                                         headshot2 = information_lst[1][8], accur20 = information_lst[1][7][0][0],
                                         accur21 = information_lst[1][7][1][0], accur22 = information_lst[1][7][2][0],
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg",
                                         kd3 = information_lst[2][3], win_rate3 = information_lst[2][2], adr3 = information_lst[2][4],
                                         headshot3 = information_lst[2][8], accur30 = information_lst[2][7][0][0],
                                         accur31 = information_lst[2][7][1][0], accur32 = information_lst[2][7][2][0],
                                         weapon_img10 = f"{information_lst[0][7][0][1]}.png", weapon_img11 = f"{information_lst[0][7][1][1]}.png",
                                         weapon_img12 = f"{information_lst[0][7][2][1]}.png", weapon_img20 = f"{information_lst[1][7][0][1]}.png",
                                         weapon_img21 = f"{information_lst[1][7][1][1]}.png", weapon_img22 = f"{information_lst[1][7][2][1]}.png",
                                         weapon_img30 = f"{information_lst[2][7][0][1]}.png", weapon_img31 = f"{information_lst[2][7][1][1]}.png",
                                         weapon_img32 = f"{information_lst[2][7][2][1]}.png")
    if len(information_lst) == 4:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         kd = information_lst[0][3], win_rate = information_lst[0][2], adr = information_lst[0][4],
                                         headshot = information_lst[0][8], accur = information_lst[0][7][0][0],
                                         accur2 = information_lst[0][7][1][0], accur3 = information_lst[0][7][2][0],
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         kd2 = information_lst[1][3], win_rate2 = information_lst[1][2], adr2 = information_lst[1][4],
                                         headshot2 = information_lst[1][8], accur20 = information_lst[1][7][0][0],
                                         accur21 = information_lst[1][7][1][0], accur22 = information_lst[1][7][2][0],
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg",
                                         kd3 = information_lst[2][3], win_rate3 = information_lst[2][2], adr3 = information_lst[2][4],
                                         headshot3 = information_lst[2][8], accur30 = information_lst[2][7][0][0],
                                         accur31 = information_lst[2][7][1][0], accur32 = information_lst[2][7][2][0],
                                         your_name4 = information_lst[3][0], source_img4 = f"{information_lst[3][1]}.jpg",
                                         kd4 = information_lst[3][3], win_rate4 = information_lst[3][2], adr4 = information_lst[3][4],
                                         headshot4 = information_lst[3][8], accur40 = information_lst[3][7][0][0],
                                         accur41 = information_lst[2][7][1][0], accur42 = information_lst[3][7][2][0],
                                         weapon_img10 = f"{information_lst[0][7][0][1]}.png", weapon_img11 = f"{information_lst[0][7][1][1]}.png",
                                         weapon_img12 = f"{information_lst[0][7][2][1]}.png", weapon_img20 = f"{information_lst[1][7][0][1]}.png",
                                         weapon_img21 = f"{information_lst[1][7][1][1]}.png", weapon_img22 = f"{information_lst[1][7][2][1]}.png",
                                         weapon_img30 = f"{information_lst[2][7][0][1]}.png", weapon_img31 = f"{information_lst[2][7][1][1]}.png",
                                         weapon_img32 = f"{information_lst[2][7][2][1]}.png", weapon_img40 = f"{information_lst[3][7][0][1]}.png",
                                         weapon_img41 = f"{information_lst[3][7][1][1]}.png", weapon_img42 = f"{information_lst[3][7][2][1]}.png")
    if len(information_lst) == 5:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         kd = information_lst[0][3], win_rate = information_lst[0][2], adr = information_lst[0][4],
                                         headshot = information_lst[0][8], accur = information_lst[0][7][0][0],
                                         accur2 = information_lst[0][7][1][0], accur3 = information_lst[0][7][2][0],
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         kd2 = information_lst[1][3], win_rate2 = information_lst[1][2], adr2 = information_lst[1][4],
                                         headshot2 = information_lst[1][8], accur20 = information_lst[1][7][0][0],
                                         accur21 = information_lst[1][7][1][0], accur22 = information_lst[1][7][2][0],
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg",
                                         kd3 = information_lst[2][3], win_rate3 = information_lst[2][2], adr3 = information_lst[2][4],
                                         headshot3 = information_lst[2][8], accur30 = information_lst[2][7][0][0],
                                         accur31 = information_lst[2][7][1][0], accur32 = information_lst[2][7][2][0],
                                         your_name4 = information_lst[3][0], source_img4 = f"{information_lst[3][1]}.jpg",
                                         kd4 = information_lst[3][3], win_rate4 = information_lst[3][2], adr4 = information_lst[3][4],
                                         headshot4 = information_lst[3][8], accur40 = information_lst[3][7][0][0],
                                         accur41 = information_lst[2][7][1][0], accur42 = information_lst[3][7][2][0],
                                         your_name5 = information_lst[4][0], source_img5 = f"{information_lst[4][1]}.jpg",
                                         kd5 = information_lst[4][3], win_rate5 = information_lst[4][2], adr5 = information_lst[4][4],
                                         headshot5 = information_lst[4][8], accur50 = information_lst[4][7][0][0],
                                         accur51 = information_lst[4][7][1][0], accur52 = information_lst[4][7][2][0],
                                         weapon_img10 = f"{information_lst[0][7][0][1]}.png", weapon_img11 = f"{information_lst[0][7][1][1]}.png",
                                         weapon_img12 = f"{information_lst[0][7][2][1]}.png", weapon_img20 = f"{information_lst[1][7][0][1]}.png",
                                         weapon_img21 = f"{information_lst[1][7][1][1]}.png", weapon_img22 = f"{information_lst[1][7][2][1]}.png",
                                         weapon_img30 = f"{information_lst[2][7][0][1]}.png", weapon_img31 = f"{information_lst[2][7][1][1]}.png",
                                         weapon_img32 = f"{information_lst[2][7][2][1]}.png", weapon_img40 = f"{information_lst[3][7][0][1]}.png",
                                         weapon_img41 = f"{information_lst[3][7][1][1]}.png", weapon_img42 = f"{information_lst[3][7][2][1]}.png",
                                         weapon_img50 = f"{information_lst[4][7][0][1]}.png", weapon_img51 = f"{information_lst[4][7][1][1]}.png",
                                         weapon_img52 = f"{information_lst[4][7][2][1]}.png")


@app.route("/new2", methods = ['POST'])
def register2():
    global information_lst
    global counter
    global add_info
    global exemplar
    param = 0

    our_map = request.form.get('Map')
    enemy_side = request.form.get('side')

    print(our_map, enemy_side)

    if add_info == []:
        add_info = [our_map, enemy_side]


    if counter == 16 and add_info[1] == "CT":
        add_info[1] = "TT"
    
    elif counter == 16 and add_info[1] == "TT":
        add_info[1] = "CT"

    win_side = int(request.form.get('win_side'))
    end_round = int(request.form.get('end_round'))
    bomb_planted = int(request.form.get('bomb_planted'))
    mates_alive = int(request.form.get('mates_alive'))
    enemies_alive = int(request.form.get('enemies_alive'))
    enemies_buy = int(request.form.get('enemies_buy'))
    knife_kills = int(request.form.get('knife_kills'))

    if counter == 1 and not param: 
        exemplar = RecomendationADT(add_info[0], add_info[1]) 
    if counter < 16: 
        exemplar.process(win_side, end_round, bomb_planted, enemies_alive, mates_alive, enemies_buy, knife_kills) 
        advice = exemplar.advice() 
    else: 
        counter = 0 
        exemplar = RecomendationADT(add_info[0], add_info[1])
        exemplar.process(win_side, end_round, bomb_planted, enemies_alive, mates_alive, enemies_buy, knife_kills) 
        advice = exemplar.advice()
        param = 1
    print(advice)
    counter +=1

    print("-----------------------------------------------")
    if len(information_lst) == 0:
        return render_template("1.html")
    if len(information_lst) == 1:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg", information = advice)
    if len(information_lst) == 2:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg", information = advice)
    if len(information_lst) == 3:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg", information = advice)
    if len(information_lst) == 4:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg",
                                         your_name4 = information_lst[3][0], source_img4 = f"{information_lst[3][1]}.jpg", information = advice)
    if len(information_lst) == 5:
        return render_template("1.html", your_name = information_lst[0][0], source_img = f"{information_lst[0][1]}.jpg",
                                         your_name2 = information_lst[1][0], source_img2 = f"{information_lst[1][1]}.jpg",
                                         your_name3 = information_lst[2][0], source_img3 = f"{information_lst[2][1]}.jpg",
                                         your_name4 = information_lst[3][0], source_img4 = f"{information_lst[3][1]}.jpg",
                                         your_name5 = information_lst[4][0], source_img5 = f"{information_lst[4][1]}.jpg", information = advice)


if __name__ == "__main__":
    app.run(debug=False)