const likeLink = document.querySelector("span a.link-success");
const likesAmount = document.querySelector("span.likes");

document.addEventListener("DOMContentLoaded", () => {
  const newIcon = document.createElement("i");
  const oldIcon = likeLink.querySelector("i");
  switch (likeLink.dataset.action) {
    case "like":
      newIcon.className = "bi bi-hand-thumbs-up";
      break;
    case "unlike":
      newIcon.className = "bi bi-hand-thumbs-up-fill";
      likesAmount.classList.add("bg-success");
      break;
  }

  likeLink.removeChild(oldIcon);
  likeLink.appendChild(newIcon);
});

likeLink.addEventListener("click", (event) => {
  event.preventDefault();

  const id = likeLink.dataset.id;
  const action = likeLink.dataset.action;
  const url = likeLink.dataset.url;

  likeImage(url, id, action)
    .then((response) => {
      console.log(response);
      changeLikeState(action);
    })
    .catch((err) => console.error(err));
});

function likeImage(url, image_id, image_action) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const csrfToken = Cookies.get("csrftoken");

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.responseType = "json";

    xhr.addEventListener("load", () => {
      if ((xhr.status >= 200) & (xhr.status < 300)) {
        resolve(xhr.response);
      } else {
        reject(xhr.response);
      }
    });

    xhr.send(`id=${image_id}&action=${image_action}`);
  });
}

function changeLikeState(action) {
  if (action == "unlike") {
    likeLink.dataset.action = "like";
    likesAmount.innerHTML--;
    likesAmount.classList.remove("bg-success");
  } else {
    likesAmount.innerHTML++;
    likeLink.dataset.action = "unlike";
    likesAmount.classList.add("bg-success");
  }

  changeThumbIcon(action);
}

function changeThumbIcon(action) {
  const newIcon = document.createElement("i");

  switch (action) {
    case "like":
      newIcon.className = "bi bi-hand-thumbs-up-fill";
      break;
    case "unlike":
      newIcon.className = "bi bi-hand-thumbs-up";
      break;
    default:
      throw new Error(`Wrong action given - ${action}`);
  }

  likeLink.innerHTML = "";
  likeLink.appendChild(newIcon);

  return newIcon;
}
