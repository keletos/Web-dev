function addItem() 
{
    let input = document.getElementById("inputText");
    let text = input.value.trim();
    if (text === "") return;

    let div = document.createElement("div");
    div.classList.add("item");

    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    let label = document.createElement("label");
    label.textContent = text;

    checkbox.onchange = function() {
        label.classList.toggle("checked", checkbox.checked);
    };

    let button = document.createElement("button");
    button.textContent = "Удалить";
    button.classList.add("delete-btn");
    button.onclick = function() {
        div.remove();
    };

    div.appendChild(checkbox);
    div.appendChild(label);
    div.appendChild(button);
    document.getElementById("checkboxList").appendChild(div);

    input.value = "";
}