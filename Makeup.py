from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/<page>')
def dynamic_page(page):
    if page == 'makeup':
        return render_template('makeup.html', makeup=page)
    elif page == 'clothes':
        return render_template('clothes.html', clothes=page)
    elif page == 'bodytypes':
        return render_template('bodytypecal.html', bodytypes=page)
    elif page == 'hairstyles':
        return render_template('hair.html', hairstyles=page)
    else:
        return "Page not found",404

app.run(debug=True)