// This event is triggered after the page is loaded
document.addEventListener("DOMContentLoaded", function () {
  const data = [
    { name: "Item 1", description: "This is the first item.", date: "2025/05/09"},
    { name: "Item 2", description: "This is the second item.", date: "2025/05/25" },
    { name: "Item 3", description: "This is the third item.", date: "1995/12/16" }
  ];

  const container = document.getElementById("filesList");

  data.forEach(item => {
    const div = document.createElement("div");
    div.className = "listElement";
    div.innerHTML = `<span class="material-symbols-outlined">favorite</span> ${item.name} ${item.description} ${item.date}`;
    container.appendChild(div);
  });
});