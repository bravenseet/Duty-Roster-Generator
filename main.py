from flask import Flask, render_template, request
import m

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def home():
  if request.method == 'POST':
    #marker
    m1 = request.form['m1']
    m2 = request.form['m2']
    m3 = request.form['m3']
    m4 = request.form['m4']
    m5 = request.form['m5']

    #nat flag
    nf1 = request.form['nf1']
    nf2 = request.form['nf2']
    nf3 = request.form['nf3']
    nf4 = request.form['nf4']
    nf5 = request.form['nf5']

    #sch flag
    sf1 = request.form['sf1']
    sf2 = request.form['sf2']
    sf3 = request.form['sf3']
    sf4 = request.form['sf4']
    sf5 = request.form['sf5']

    #foyer hostel
    fh1 = request.form['fh1']
    fh2 = request.form['fh2']
    fh3 = request.form['fh3']
    fh4 = request.form['fh4']
    fh5 = request.form['fh5']

    #foyer latecomer
    fl1 = request.form['fl1']
    fl2 = request.form['fl2']
    fl3 = request.form['fl3']
    fl4 = request.form['fl4']
    fl5 = request.form['fl5']

    #guardhouse
    gh1 = request.form['gh1']
    gh2 = request.form['gh2']
    gh3 = request.form['gh3']
    gh4 = request.form['gh4']
    gh5 = request.form['gh5']

    #gate a
    ga1 = request.form['ga1']
    ga2 = request.form['ga2']
    ga3 = request.form['ga3']
    ga4 = request.form['ga4']
    ga5 = request.form['ga5']

    #gate b
    gb1 = request.form['gb1']
    gb2 = request.form['gb2']
    gb3 = request.form['gb3']
    gb4 = request.form['gb4']
    gb5 = request.form['gb5']

    #lift 1
    lI1 = request.form['lI1']
    lI2 = request.form['lI2']
    lI3 = request.form['lI3']
    lI4 = request.form['lI4']
    lI5 = request.form['lI5']

    #lift 2
    lII1 = request.form['lII1']
    lII2 = request.form['lII2']
    lII3 = request.form['lII3']
    lII4 = request.form['lII4']
    lII5 = request.form['lII5']

    #canteen
    ca1 = request.form['ca1']
    ca2 = request.form['ca2']
    ca3 = request.form['ca3']
    ca4 = request.form['ca4']
    ca5 = request.form['ca5']

    #lp
    lp1 = request.form['lp1']
    lp2 = request.form['lp2']
    lp3 = request.form['lp3']
    lp4 = request.form['lp4']
    lp5 = request.form['lp5']
    ####################

    # marker
    m.dutyset(m.markerduty, m.marker_duty, int(m1), int(m2), int(m3), int(m4),
              int(m5))
    # nat flag
    m.dutyset(m.natflag, m.nat_flag_duty, int(nf1), int(nf2), int(nf3),
              int(nf4), int(nf5))
    #sch flag
    m.dutyset(m.schflag, m.sch_flag_duty, int(sf1), int(sf2), int(sf3),
              int(sf4), int(sf5))

    #foyerhostel
    m.normalduty(m.foyerhostel, int(fh1), int(fh2), int(fh3), int(fh4),
                 int(fh5))

    #foyer latecomer
    m.normalduty(m.foyerlate, int(fl1), int(fl2), int(fl3), int(fl4), int(fl5))

    #guardhouse
    m.normalduty(m.guardhouse, int(gh1), int(gh2), int(gh3), int(gh4),
                 int(gh5))

    #gate a
    m.normalduty(m.gatea, int(ga1), int(ga2), int(ga3), int(ga4), int(ga5))

    #gate b
    m.normalduty(m.gateb, int(gb1), int(gb2), int(gb3), int(gb4), int(gb5))

    #lift 1
    m.normalduty(m.lift1, int(lI1), int(lI2), int(lI3), int(lI4), int(lI5))

    #lift 2
    m.normalduty(m.lift2, int(lII1), int(lII2), int(lII3), int(lII4),
                 int(lII5))

    #canteen
    m.normalduty(m.canteen, int(ca1), int(ca2), int(ca3), int(ca4), int(ca5))

    #lp
    m.normalduty(m.levelpatrol, int(lp1), int(lp2), int(lp3), int(lp4),
                 int(lp5))

  return render_template('index.html',
                         md=m.markerduty,
                         nf=m.natflag,
                         sf=m.schflag,
                         fl=m.foyerlate,
                         fh=m.foyerhostel,
                         gdh=m.guardhouse,
                         ga=m.gatea,
                         gb=m.gateb,
                         l1=m.lift1,
                         l2=m.lift2,
                         ca=m.canteen,
                         lp=m.levelpatrol)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
