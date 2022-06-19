const actionsBlock = document.querySelector(".actions");

const url = actionsBlock.dataset.content;
let nextPage = 2;

const infiniteObserver = new IntersectionObserver(
  ([entry]) => {
    if (entry.isIntersecting && entry.intersectionRatio >= 0.7) {
      loadActions()
        .then((response) => {
          console.log(response);
          actionsBlock.insertAdjacentHTML("beforeend", response);
          nextPage++;
          infiniteObserver.unobserve(entry.target);
          infiniteObserver.observe(getLastImageElement());
        })
        .catch((reason) => {
          infiniteObserver.unobserve(entry.target);
          console.error(reason);
        });
    }
  },
  {
    threshold: 0.7,
  }
);

infiniteObserver.observe(getLastImageElement());

function loadActions() {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const urlWithPage = url + `?page=${nextPage}`;
    xhr.open("get", urlWithPage, true);

    xhr.addEventListener("load", () => {
      if (xhr.response) {
        resolve(xhr.response);
      } else {
        reject("Empty page");
      }
    });

    xhr.send();
  });
}

function getLastImageElement() {
  return actionsBlock.querySelector("div.col-12:last-child");
}
