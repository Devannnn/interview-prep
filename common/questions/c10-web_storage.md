# What is the difference between localStorage, sessionStorage, and cookies?

Localstorage, sessionStorage and cookies are all ways to store user-specific data to provide a more custom experience.

LocalStorage is a local storage for your browser. It stores data permanently which means those data are persisted between page reloads and browser restarts. It can save as much as 10 Mb. It's not cleared automatically - the cache needs to be cleared. Only the client-side reads this storage.

SessionStorage stores data temporarily, until you close the tab or the window. It's a bit smaller - 5 Mb. Only the client-side reads this storage.

Cookies are very tiny data - 4 Kb - stored in the browser and which are sent to the server at each HTTP request.