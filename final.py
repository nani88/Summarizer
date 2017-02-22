from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
import Algorithmia
apiKey = "simJyJaH8sR1EEq+6EqwRfLtquW1"
client=Algorithmia.client(apiKey)

@app.route('/summarize/',methods=['GET','POST'])
def summarizeCode():
    if request.method=='POST':
        input=request.form['text']
        algo=client.algo('nlp/Summarizer/0.1.3')
        response=algo.pipe(request.form['text']).result
        return render_template('summary.html',response=response,input=input)
    else:
        return render_template('summarizerform.html')

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
