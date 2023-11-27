// =====*===== POPUP SCRIPTS =====*===== //
const popup = document.querySelector(".popup");
// popup toggle
popupToggle = () => {
  popup.classList.toggle("active");
};

// hide popup when click outside
document.addEventListener("mouseup", function (e) {
  if (!popup.contains(e.target)) {
    popup.classList.remove("active");
  }
});

// =====*===== LATIN BUTTON SCRIPTS =====*===== //
// adding characters to the input field
// add = (param) => {
//   let input = document.getElementById("latin_input");
//   input.value += param;
// };
// adding characters to where the cursor is
add = (param) => {
  let input = document.getElementById("latin_input");
  let cursorPos = input.selectionStart;
  let v = input.value;
  let textBefore = v.substring(0, cursorPos);
  let textAfter = v.substring(cursorPos, v.length);
  input.value = textBefore + param + textAfter;
  input.selectionStart = cursorPos + param.length;
  input.selectionEnd = cursorPos + param.length;
  input.focus();
};

// when button download clicked, display the download popup
const donwloadPopup = document.querySelector(".download_popup");
donwload = () => {
  donwloadPopup.classList.toggle("active");
};
