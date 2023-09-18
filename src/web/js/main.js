document.getElementById("button-spanish").addEventListener("click", () => { eel.choose_language("es") }, false);
document.getElementById("button-english").addEventListener("click", () => { eel.choose_language("en") }, false);
document.getElementById("load-mics").addEventListener("click", () => { eel.show_mics() }, false);
document.getElementById("select-mic").addEventListener("change", () => { 
  console.log(document.getElementById("select-mic").value);
  eel.select_mic(document.getElementById("select-mic").value);
}, false);

function show_subtitles(subtitles) {
  document.getElementById("subtitles-text").innerHTML = subtitles;
}

function show_translation(translation) {
  document.getElementById("translation-text").innerHTML = translation;
}

function fill_select_mics(mics) {
  mics = JSON.parse(mics);

  let select = document.getElementById("select-mic");
  mics.mics_id.forEach((mic_id, index) => {
    let option = document.createElement("option");
    option.value = mic_id;
    option.text = mics.mics_name[index];
    select.appendChild(option);
  });
}

eel.expose(show_subtitles);
eel.expose(show_translation);
eel.expose(fill_select_mics);