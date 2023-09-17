document.getElementById("button-spanish").addEventListener("click", ()=>{eel.choose_language("es")}, false);
document.getElementById("button-english").addEventListener("click", ()=>{eel.choose_language("en")}, false);


function show_subtitles(subtitles) {
  document.getElementById("subtitles-text").innerHTML = subtitles;
}

function show_translation(translation) {
  document.getElementById("translation-text").innerHTML = translation;
}

eel.expose(show_subtitles);
eel.expose(show_translation);