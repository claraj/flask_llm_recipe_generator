from flask import Flask, request, render_template, flash, redirect, abort
import recipe_llm 


app = Flask(__name__)
app.secret_key = '12345678'  # Real app needs a long random key, stored outside the code

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    ingredients = request.form.to_dict().get('ingredients')
    if not ingredients or ingredients.strip() == '':
        flash('You must enter an ingredient')
        return redirect('/')
        
    recipe, error = recipe_llm.generate_recipe(ingredients)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    else:
        abort(500)
    

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)