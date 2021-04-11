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


@app.route('/upload')
@app.route('/drop')
def drop():
    return redirect(f'https://drop.fumaz.dev')


if __name__ == '__main__':
    app.run('0.0.0.0')
