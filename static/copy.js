document.getElementById("quizUrl").value = window.location.href;

function CopyFunc() {
    var copyText = document.getElementById("quizUrl");
    copyText.value = window.location.href;
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document.execCommand("copy");
    alert("Copied the Url: " + copyText.value);
}