import { set } from "react-hook-form";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      user: {},
      posts: [],
      access_token: null,
    },
    actions: {
      getPosts: async () => {
        const store = getStore();

        fetch(process.env.BACKEND_URL + "/posts")
          .then((resp) => resp.json())
          .then((data) => {
            console.log(data.all_posts);
            setStore({
              posts: data.all_posts,
            });
            console.log(store.posts);
          })
          .catch((error) =>
            console.log("Error loading message from backend", error)
          );
      },
      addPost: (post) => {
        const store = getStore();
        let requestOptions = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${store.access_token}`,
          },
          body: JSON.stringify({
            text: post.text,
          }),
        };

        fetch(process.env.BACKEND_URL + "/create_post", requestOptions)
          .then((response) => response.json())
          .then((result) => {
            const newArray = store.posts.concat([result.post]);
            setStore({ ...store, posts: newArray });
          })
          .catch((error) => console.log("error", error));
      },

      register: (data) => {
        let requestOptions = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: data.email,
            password: data.password,
            first_name: data.first_name,
            last_name: data.last_name,
          }),
        };

        fetch(process.env.BACKEND_URL + "/register", requestOptions)
          .then((res) => {
            res.json();
          })
          .then((data) => {
            console.log(data);
          })
          .catch((err) => err);
      },

      login: async (data) => {
        const store = getStore();
        let requestOptions = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: data.email,
            password: data.password,
          }),
        };

        let resp = await fetch(
          process.env.BACKEND_URL + "/login",
          requestOptions
        );
        if (resp.status === 200) {
          try {
            let data = await resp.json();
            setStore({ user: data.user });
            setStore({ access_token: data.access_token });
            console.log(store.user);
            return true;
          } catch {
            console.log("an error occurred while logging in");
          }
        } else {
          console.log(resp);
        }
      },
    },
  };
};

export default getState;
