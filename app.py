from flask import Flask , jsonify

todo=Flask(__name__)

students = [
    {
        'id':1,
        'name':'AAA',
        'age':10
    },
    {
        'id':2,
        'name':'BBB',
        'age':10
    }
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for student in students:
        if student['id']==id:
            return jsonify(student)
        print(student)
    return jsonify('not found')


if __name__=='__main__':
    todo.run(
        host='127.0.0.1',
        port=5011,
        debug=True
    )