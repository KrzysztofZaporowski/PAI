function isEmpty(str) {
  if (str.length == 0) {
    return true;
  }
  return false;
}

function isWhiteSpaceOrEmpty(str) {
  return /^[\s\t\r\n]*$/.test(str);
}

function checkString(str, msg) {
  if (isEmpty(str) || isWhiteSpaceOrEmpty(str)) {
    //alert(msg);
    return false;
  }
  return true;
}

function checkEmail(str) {
  let email = /^[a-zA-Z_0-9\.]+@[a-zA-Z_0-9\.]+\.[a-zA-Z][a-zA-Z]+$/;
  if (email.test(str)) return true;
  else {
    //alert("Podaj właściwy e-mail");
    return false;
  }
}

// function checkStringAndFocus(obj, msg) {
//   let str = obj.value;
//   let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
//   if (isWhiteSpaceOrEmpty(str)) {
//     document.getElementById(errorFieldName).innerHTML = msg;
//     obj.focus();
//     return false;
//   } else {
//     document.getElementById(errorFieldName).innerHTML = "";
//     return true;
//   }
// }

// function checkEmailAndFocus(obj, msg) {
//   let str = obj.value;
//   let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
//   if (!checkEmail(str)) {
//     document.getElementById(errorFieldName).innerHTML = msg;
//     obj.focus();
//     return false;
//   } else {
//     document.getElementById(errorFieldName).innerHTML = "";
//     return true;
//   }
// }

function checkStringAndFocus(obj, msg, functionToCall) {
  let str = obj.value;
  let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
  if (!functionToCall(str)) {
    document.getElementById(errorFieldName).innerHTML = msg;
    obj.focus();
    return false;
  } else {
    document.getElementById(errorFieldName).innerHTML = "";
    return true;
  }
}

function validate(form) {
  return (
    checkStringAndFocus(form.elements["f_imie"], "Podaj imię!", checkString) &&
    checkStringAndFocus(
      form.elements["f_nazwisko"],
      "Podaj nazwisko!",
      checkString,
    ) &&
    checkStringAndFocus(
      form.elements["f_email"],
      "Podaj prawidłowy e-mail!",
      checkEmail,
    ) &&
    checkStringAndFocus(
      form.elements["f_kod"],
      "Podaj kod pocztowy!",
      checkString,
    ) &&
    checkStringAndFocus(form.elements["f_miasto"], "Podaj miasto!", checkString)
  );
}

//TODO: od punktu 21
