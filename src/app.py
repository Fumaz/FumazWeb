from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/twitch')
def twitch():
    return redirect('https://twitch.tv/FumazDev')


@app.route('/discord')
def discord():
    return redirect('https://discord.gg/kSqXdGpYVB')


@app.route('/youtube')
def youtube():
    return redirect('https://www.youtube.com/channel/UCtSNeK8-HLYKsOW2x0J25DQ')


@app.route('/patreon')
def patreon():
    return redirect('https://www.patreon.com/Fumaz')


@app.route('/twitter')
def twitter():
    return redirect('https://twitter.com/FumazDev')


@app.route('/texturepack')
def texture_pack():
    return redirect('https://s.fumaz.dev/JKYOY')


@app.route('/github')
def github():
    return redirect('https://github.com/Fumaz')


@app.route('/reddit')
def reddit():
    return redirect('https://reddit.com/r/Fumaz')


@app.route('/')
@app.errorhandler(Exception)
def index(_=None):
    return render_template('index.html')


@app.route('/c/<filename>')
def cloud(filename: str):
    return redirect(f'https://cloud.fumaz.dev/s/{filename}/download')


@app.route('/cw/<filename>')
def preview(filename: str):
    return redirect(f'https://cloud.fumaz.dev/s/{filename}')


@app.route('/p/<path>')
@app.route('/p')
@app.route('/p/')
def paste(path: str = ''):
    return redirect(f'https://paste.fumaz.dev/{path}')


@app.route('/s/<path>')
def shortener(path: str):
    return redirect(f'https://s.fumaz.dev/{path}')


@app.route('/upload')
@app.route('/drop')
def drop():
    return redirect(f'https://drop.fumaz.dev')


@app.route('/customers')
def customers():
    return render_template('customers.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
