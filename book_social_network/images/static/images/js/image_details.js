const thumbUpButton = document.querySelector("span a.link-success");
const likesAmount = document.querySelector;

thumbUpButton.addEventListener("click", (event) => {
  const id = thumbUpButton.dataset.id;
  const action = thumbUpButton.dataset.action;
  const url = thumbUpButton.dataset.url;

  likeImage(url, id, action);
});

function likeImage(url, image_id, image_action) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  console.log(xhr.send(`id=${image_id}&action=${image_action}`));
}
