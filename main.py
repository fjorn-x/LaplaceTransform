from flask import Flask, render_template
from flask.globals import request
import func

app=Flask("__name__")

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/operation_result/',methods=['POST'])
def operation_result() :
    first_input=request.form['Input1']
    second_input=request.form['Input2']
    operation=request.form['operation']
    try:
        input1=int(first_input)
        input2=int(second_input)
        while True:
            if operation== 'a' :
                result_num, result_den=func.constant(input1,input2);
                break;
            elif operation=='b' :
                result_num, result_den=func.expo(input1,input2);
                break;
            elif operation=='c' :
                result=str(func.sine(input1,input2));
                break;
            elif operation=='d' :
                result=str(func.cos(input1,input2))
                break;
            elif operation=='e' :
                result=str(func.tfunc(input1,input2))
                break;
            elif operation=='f' :
                result=str(func.expo_cos(input1,input2))
                break;
            elif operation=='g' :
                result=str(func.expo_sin(input1,input2))
                break;
            elif operation=='h' :
                result=str(func.t_expo(input1,input2))
                break;
            elif operation=='i' :
                result=str(func.expo_sinh(input1,input2))
                break;
            elif operation=='j' :
                result=str(func.expo_cosh(input1,input2))
                break;
            elif operation =='k' :
                result=str(func.sinh(input1,input2))
                break;
            elif operation =='l' :
                result=str(func.cosh(input1,input2))
                break;
       
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result_num=result_num,
            result_den=result_den,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result2='Bad Input',
            calculation_success=False,
            error="You cannot divide by zero"
        )
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result3='Bad Input',
            calculation_success=False,
            error="Cannot perform operations with provided inputs"
        )
  
@app.route('/information')
def info() :
    return render_template('information.html')

@app.route('/about')
def about() :
    return render_template('about.html')

    
if __name__=="__main__" :
    app.run(debug=True,host="localhost")
