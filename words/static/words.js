function clear_field(field_id) {
  const field = document.getElementById(field_id)
  field.value = "";
  field.focus();
}

function set_length(length) {
  const form_id = 'words-form';
  const length_field_id = 'length';
  const letters_field_id = 'letters';
  const length_field = document.getElementById(length_field_id);
  const letters_field = document.getElementById(letters_field_id);
  length_field.value = length;
  if (letters_field.value.length != 0) {
    const form = document.getElementById(form_id);
    form.submit();
  }
}

function select_lang(language) {
  const form_id = 'words-form';
  const length_field_id = 'length';
  const letters_field_id = 'letters';
  const length_field = document.getElementById(length_field_id);
  const letters_field = document.getElementById(letters_field_id);
  const language_field_id = 'language';
  const language_field = document.getElementById(language_field_id);
  language_field.value = language;
  if (letters_field.value.length != 0 && length_field.value.length != 0) {
    const form = document.getElementById(form_id);
    form.submit();
  } else {
    update_selected_lang();
  }
}

function update_selected_lang() {
  const language_field_id = 'language';
  const language_field = document.getElementById(language_field_id);
  selected_divs = document.getElementsByClassName("selected")
  for (let i = 0; i < selected_divs.length; i++) {
    let div = selected_divs.item(i);
    if (div.id == language_field.value) {
      div.classList.add("visible");
      div.classList.remove("invisible");
    } else {
      div.classList.remove("visible");
      div.classList.add("invisible");
    }
  }
}

window.addEventListener("load", update_selected_lang);

let btns_lang = document.querySelectorAll(".btn-lang");
btns_lang.forEach(btn => {
	btn.addEventListener("click", (event) => {
		select_lang(event.target.id.replace(/^btn-/, ""));
	});
});

let btns_length = document.querySelectorAll(".btn-length");
btns_length.forEach(btn => {
	btn.addEventListener("click", (event) => {
		set_length(event.target.id.replace(/^btn-/, ""));
	});
});

let btns_clear = document.querySelectorAll(".btn-clear");
btns_clear.forEach(btn => {
	btn.addEventListener("click", (event) => {
		clear_field(event.target.id.replace(/^clear-/, ""));
	});
});
