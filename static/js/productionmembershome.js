function showAllMembers() {
  var workblock = document.getElementById("workblock");
  var UsersData = document.getElementById("UsersData");

  UsersData.style.display = "block";
  workblock.style.display = "none";
}

function DoWork(task_date, module_name, pcb_types, device_id) {
  var workblock = document.getElementById("workblock");
  var UsersData = document.getElementById("UsersData");

  UsersData.style.display = "none";
  workblock.style.display = "block";

  var cbxShowYear = document.getElementById('cbxShowYear')
  if(cbxShowYear.checked == true){
      cbxShowYear.checked = false;
  }

  var pcb_types = (document.getElementById("pcb_types").innerHTML =
    " : " + pcb_types);
  var module_name = (document.getElementById("module_name").innerHTML =
    " : " + module_name);
  var date = (document.getElementById("date").innerHTML = " : " + task_date);
  var device_id = (document.getElementById("device_id").innerHTML =
    " : " + device_id);
}

function WorkDone() {
  var span_Text = document.getElementById("display").innerText;

  var cbxShowYear = document.getElementById("cbxShowYear");
  if (cbxShowYear.checked == false) {
    NotifyUser();
  } else {
    var pcb_types = document.getElementById("pcb_types").innerText;
    var module_name = document.getElementById("module_name").innerText;
    var date = document.getElementById("date").innerText;
    var device_id = document.getElementById("device_id").innerText;

    window.location = "{% url '/productionUser/assign_visual_inspection' device_id %}"
}
}

function NotifyUser() {
  Swal.fire({
    icon: "error",
    title: "Oops...",
    text: "The work is pending not yet done please done the work first",
  });
}
