function OpenForm(){
    var parentclass = document.getElementById('parentclass')
    var addclientbtn = document.getElementById('addclientbtn')
    var formdiv = document.getElementById('formdiv')

    parentclass.style.display = 'none';
    addclientbtn.style.display = 'none';
    formdiv.style.display = 'block';

}


function openUserData(){
    var parentclass = document.getElementById('parentclass')
    var addclientbtn = document.getElementById('addclientbtn')
    var editformdiv = document.getElementById('editformdiv')
    var formdiv = document.getElementById('formdiv')

    parentclass.style.display = 'block';
    addclientbtn.style.display = 'block';
    editformdiv.style.display = 'none';
    formdiv.style.display = 'none';

}