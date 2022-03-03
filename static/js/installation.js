function OpenForm(){
    var parentclass = document.getElementById('parentclass')
    var addclientbtn = document.getElementById('addclientbtn')
    var formdiv = document.getElementById('formdiv')

    parentclass.style.display = 'none';
    addclientbtn.style.display = 'none';
    formdiv.style.display = 'block';

}

function editUser(u_name, u_email, u_password, u_designation, u_user_dept, u_is_active){
    var parentclass = document.getElementById('parentclass')
    var addclientbtn = document.getElementById('addclientbtn')
    var formdiv = document.getElementById('formdiv')

    parentclass.style.display = 'none';
    addclientbtn.style.display = 'none';
    formdiv.style.display = 'block';

    var name = document.getElementById('name')
    var email = document.getElementById('email')
    var password = document.getElementById('password')
    var designation = document.getElementById('designation')
    var user_dept = document.getElementById('user_dept')
    var is_active = document.getElementById('is_active')

    name.value = u_name
    email.value = u_email
    password.value = u_password
    designation.value = u_designation
    user_dept.value = u_user_dept
    is_active.value = u_is_active
}