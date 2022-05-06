from flask import Flask, render_template

app = Flask(__name__)

pitches =[
    {
        'author':'Mike will',
        'title':'UX Design',
        'pitch':'Did you know that the best payment milestones are dependent on your delivery and not on client approval?',
        'posted':'03/02/2020'
        
    },
    {
        'author':'Mint',
        'title':'Product Design',
        'pitch':'Designing a product is a very broad concept, it is essentially the efficient ',
        'posted':'12/02/2021'
    },
    {
        'author':'Juice',
        'title':'Interview',
        'pitch':'The executive engaged in the normal conduct of business devotes much of his time to interviewing. ',
        'posted':'22/04/2022'
        
    }    
]

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


    
    