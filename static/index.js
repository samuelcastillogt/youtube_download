const container =   document.getElementById("result")
const button = document.getElementById("search");
const categoria = document.getElementById("categoria");
const url = document.getElementById("url");
categoria.addEventListener("change", () => {
  button.toggleAttribute("disabled");
});
button.addEventListener("click", async () => {
  const response = await fetch("/", {
    method: "POST",
    body: JSON.stringify({ username: url.value, type: Number(categoria.value) }),
    headers: { "Content-Type": "application/json" },
  });
  const result = await response.json();
  HTMLInjector(result)
});

const HTMLInjector = (result)=>{
  if(Number(categoria.value <= 2)){
    container.innerHTML = `<div class="card" style="width: 18rem;">
    <img src="${result.data.img}" class="card-img-top" alt="...">
    <div class="card-body">
    <h5 class="card-title">${result.data.title}</h5>
    <video controls src="${result.data.video}" width="300" height="220"/>
    </div>
    </div>`;
  }else{
    container.innerHTML = `<div class="card" style="width: 18rem;">
    <img src="${result.data.img}" class="card-img-top" alt="...">
    <div class="card-body">
    <h5 class="card-title">${result.data.title}</h5>
    <audio controls src="${result.data.video}"/>
    </div>
    </div>`;
  }
  
}
