function isEmpty(str) {
  if (str.length == 0) {
    return true;
  }
  return false;
}

function isWhiteSpaceOrEmpty(str) {
  return /^[\s\t\r\n]*$/.test(str);
}

function isStringInvalid(str, msg) {
  if (isEmpty(str) || isWhiteSpaceOrEmpty(str)) {
    //alert(msg);
    return true;
  }
  return false;
}

function isEmailInvalid(str) {
  let email = /^[a-zA-Z_0-9\.]+@[a-zA-Z_0-9\.]+\.[a-zA-Z][a-zA-Z]+$/;
  if (email.test(str)) return false;
  return true;
}

function checkStringAndFocus(obj, msg, functionToCall) {
  let str = obj.value;
  let errorFieldName = "e_" + obj.name.substr(2, obj.name.length);
  if (functionToCall(str)) {
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
    checkStringAndFocus(
      form.elements["f_imie"],
      "Podaj imię!",
      isStringInvalid,
    ) &&
    checkStringAndFocus(
      form.elements["f_nazwisko"],
      "Podaj nazwisko!",
      isStringInvalid,
    ) &&
    checkStringAndFocus(
      form.elements["f_email"],
      "Podaj prawidłowy e-mail!",
      isEmailInvalid,
    ) &&
    checkStringAndFocus(
      form.elements["f_kod"],
      "Podaj kod pocztowy!",
      isStringInvalid,
    ) &&
    checkStringAndFocus(
      form.elements["f_miasto"],
      "Podaj miasto!",
      isStringInvalid,
    )
  );
}

document.addEventListener("DOMContentLoaded", function () {
  const mezczyznaRadio = document.querySelector(
    'input[name="f_plec"][value="f_m"]',
  );
  const kobietaRadio = document.querySelector(
    'input[name="f_plec"][value="f_k"]',
  );

  function updateNazwiskoPanienskieVisibility() {
    const selectedPlec = document.querySelector('input[name="f_plec"]:checked');
    if (!selectedPlec) return;

    if (selectedPlec.value === "f_m") {
      hideElement("NazwiskoPanienskie");
    } else {
      showElement("NazwiskoPanienskie");
    }
  }

  if (mezczyznaRadio) {
    mezczyznaRadio.addEventListener(
      "change",
      updateNazwiskoPanienskieVisibility,
    );
  }
  if (kobietaRadio) {
    kobietaRadio.addEventListener("change", updateNazwiskoPanienskieVisibility);
  }

  updateNazwiskoPanienskieVisibility();
  alterRows(1, document.getElementsByTagName("tr")[0]);
});

function showElement(e) {
  document.getElementById(e).style.visibility = "visible";
}
function hideElement(e) {
  document.getElementById(e).style.visibility = "hidden";
}

function alterRows(i, e) {
  if (e) {
    if (i % 2 == 1) {
      e.setAttribute("style", "background-color: Aqua;");
    }
    e = e.nextSibling;
    while (e && e.nodeType != 1) {
      e = e.nextSibling;
    }
    alterRows(++i, e);
  }
}

function nextNode(e) {
  while (e && e.nodeType != 1) {
    e = e.nextSibling;
  }
  return e;
}

function prevNode(e) {
  while (e && e.nodeType != 1) {
    e = e.previousSibling;
  }
  return e;
}

function swapRows(b) {
  let tab = prevNode(b.previousSibling);
  let tBody = nextNode(tab.firstChild);
  let lastNode = prevNode(tBody.lastChild);
  tBody.removeChild(lastNode);
  let firstNode = nextNode(tBody.firstChild);
  tBody.insertBefore(lastNode, firstNode);
}

function cnt(form, msg, maxSize) {
  if (form.value.length > maxSize)
    form.value = form.value.substring(0, maxSize);
  else msg.innerHTML = maxSize - form.value.length;
}
