function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function cardValue(name, email, contact, city, pin_code, ctime, lead_type, lead, billing_address, shipping_address, pk) {

  var mobilecard = document.getElementById("mobilecard");
  var editLead = document.getElementById("editLead");

  mobilecard.style.display = "none";
  editLead.style.display = "block";

  var l_name = document.getElementById("l_name");
  var l_email = document.getElementById("email");
  var l_contact = document.getElementById("contact");
  var l_city = document.getElementById("city");
  var l_pin = document.getElementById("pin_code");
  var l_type = document.getElementById("lead_type");
  var l_lead = document.getElementById("lead");
  var l_billing_add = document.getElementById("billing_address");
  var l_shipping_add = document.getElementById("shipping_address");
  var lead_id = document.getElementById('lead_id');


  l_name.value = name
  l_email.value = email
  l_contact.value = contact
  l_city.value = city
  l_pin.value = pin_code
  lead_id.value = pk
  l_type.value = lead_type
  l_lead.value = lead
  l_billing_add.value = billing_address
  l_shipping_add.value = shipping_address

}

function leadEdit(name, email, contact, city, pin_code, ctime, lead_type, lead, billing_address, shipping_address, pk, ref_type, ref_name) {
  // alert(pk)
  var table_view = document.getElementById("bomVerificationSection");
  var editLead = document.getElementById("editLead");
  var addclientbtn = document.getElementById("addclientbtn");

  table_view.style.display = "none";
  addclientbtn.style.display = "none";
  editLead.style.display = "block";

  var l_name = document.getElementById("l_name");
  var l_email = document.getElementById("email");
  var l_contact = document.getElementById("contact");
  var l_city = document.getElementById("city");
  var l_pin = document.getElementById("pin_code");
  var l_type = document.getElementById("lead_type");
  var l_lead = document.getElementById("lead");
  var l_billing_add = document.getElementById("billing_address");
  var l_shipping_add = document.getElementById("shipping_address");
  var lead_id = document.getElementById('lead_id');
  var l_ref_type = document.getElementById('ref_type');
  var l_ref_name = document.getElementById('ref_name');

  l_name.value = name
  l_email.value = email
  l_contact.value = contact
  l_city.value = city
  l_pin.value = pin_code
  l_type.value = lead_type
  lead_id.value = pk
  l_lead.value = lead
  l_billing_add.value = billing_address
  l_shipping_add.value = shipping_address
  l_ref_type.value = ref_type
  l_ref_name.value = ref_name
}

function updateLead(pk){
  
  var l_name = document.getElementById("l_name").value;
  var l_email = document.getElementById("email");
  var l_contact = document.getElementById("contact");
  var l_city = document.getElementById("city");
  var l_pin = document.getElementById("pin_code");
  var l_type = document.getElementById("lead_type");
  var l_lead = document.getElementById("lead");
  var l_billing_add = document.getElementById("billing_address");
  var l_shipping_add = document.getElementById("shipping_address");

  dict = {'anike': 'a'}

  alert(dict['aniket'])
}

function openLeadDetail() {
  var table_view = document.getElementById("bomVerificationSection");
  var editLead = document.getElementById("editLead");
  var addclientbtn = document.getElementById("addclientbtn");
  var mobilecard = document.getElementById("mobilecard");

  if (mobilecard.style.display == "none") {
    mobilecard.style.display = "block";
    table_view.style.display = "none";
    addclientbtn.style.display = "none";
    editLead.style.display = "none";
  } else {
    table_view.style.display = "block";
    addclientbtn.style.display = "block";
    editLead.style.display = "none";
  }
}

// open a add note form 
function openAddNoteForm(){
  var add_note = document.getElementById('add_note');
  var notecard = document.getElementById('notecard');

  if(add_note.style.display == 'block'){
    add_note.style.display = 'none';
    notecard.style.display = 'block';
  }
  else{
    add_note.style.display = 'block';
    notecard.style.display = 'none';
  }
}

// open a all lead notes from add lead note screen
function openLeadNote(){
  var add_note = document.getElementById('add_note');
  var notecard = document.getElementById('notecard');

  add_note.style.display = 'none';
  notecard.style.display = 'block';
}

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-50px";
    }
    prevScrollpos = currentScrollPos;
}