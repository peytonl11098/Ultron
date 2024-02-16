from flask import Flask, render_template, request, redirect

app = Flask(__name__)

volunteer_list = []

selected_row = None

@app.route('/')
def index():
    return render_template('index.html', volunteer_list=volunteer_list, selected_row=selected_row)

@app.route('/submit', methods=['POST'])
def on_form_submit():
    form_data = read_form_data(request.form)
    if selected_row is None:
        insert_new_record(form_data)
    else:
        update_record(form_data)
    reset_form()
    return redirect('/')

def read_form_data(form):
    form_data = {
        "fullName": form.get("fullName"),
        "email": form.get("email"),
        "phoneNumber": form.get("phoneNumber"),
        "password": form.get("password")
    }
    return form_data

def insert_new_record(data):
    volunteer_list.append(data)

def reset_form():
    global selected_row
    selected_row = None

@app.route('/edit/<int:row_index>')
def on_edit(row_index):
    global selected_row
    selected_row = row_index
    return redirect('/')

def update_record(form_data):
    global selected_row
    volunteer_list[selected_row]["fullName"] = form_data["fullName"]
    volunteer_list[selected_row]["email"] = form_data["email"]
    volunteer_list[selected_row]["phoneNumber"] = form_data["phoneNumber"]
    volunteer_list[selected_row]["password"] = form_data["password"]

@app.route('/delete/<int:row_index>')
def on_delete(row_index):
    if row_index < len(volunteer_list):
        if confirm_delete():
            volunteer_list.pop(row_index)
            reset_form()
    return redirect('/')

def confirm_delete():
    # You can implement confirmation logic here, for now, always return True
    return True

if __name__ == '__main__':
    app.run(debug=True)
