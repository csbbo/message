const removeCookie = (key) => {
  document.cookie = `${key}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT`
}

export {
  removeCookie
}