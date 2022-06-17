const followButton = document.querySelector("button.follow");

followButton.addEventListener("click", () => {
  followUser()
    .then((response) => {
      changeButtonState();
    })
    .catch((reason) => {
      console.error(reason);
    });
});

function followUser() {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("post", followButton.dataset.url, true);

    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
    xhr.responseType = "json";

    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(xhr.response);
      } else {
        reject(xhr.response);
      }
    };

    xhr.send(
      `id=${followButton.dataset.id}&action=${followButton.dataset.action}`
    );
  });
}

function changeButtonState() {
  const bootstrapStyles = ["btn", "btn-success", "btn-sm"];
  const followersAmount = document.querySelector(".followers span");

  if (followButton.dataset.action.toLowerCase() == "follow") {
    followButton.dataset.action = followButton.innerHTML = "Unfollow";
    followersAmount.innerHTML++;
    followButton.classList.remove("btn-greyblue-sm");
    bootstrapStyles.forEach((element) => {
      followButton.classList.add(element);
    });
  } else {
    followButton.dataset.action = followButton.innerHTML = "Follow";
    followersAmount.innerHTML--;
    bootstrapStyles.forEach((element) => {
      followButton.classList.remove(element);
    });
    followButton.classList.add("btn-greyblue-sm");
  }
}
