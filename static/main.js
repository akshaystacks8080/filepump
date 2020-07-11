function signupClick() {
  let curLink = window.location.href;
  let newLink = curLink + "signup";
  window.location.href = newLink;
}

function loginClick() {
  let curLink = window.location.href;
  let newLink = curLink + "login";
  window.location.href = newLink;
}

function aboutClick() {
  let curLink = window.location.href;
  let newLink = curLink + "about";
  window.location.href = newLink;
}

function fileupload() {
  let input = document.createElement("input");
  input.type = "file";

  input.onchange = (e) => {
    //console.log(e.target.files[0]);
    let file = e.target.files[0];
    let formData = new FormData();
    formData.append("uploadedFile", file);
    fetch("/upload", { method: "POST", body: formData });
  };

  input.click();
}
