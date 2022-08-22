import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { Navigate, useNavigate } from "react-router-dom";

const Wall = () => {
  const { store, actions } = useContext(Context);
  const [posts, setPosts] = useState(store.posts);
  const [user, setUser] = useState(store.user);
  const [inputValue, setInputValue] = useState("");
  let navigate = useNavigate();
  const onPost = () => {
    if (store.user.id) {
      let newPost = {
        text: inputValue,
        user_id: store.user.id,
      };
      actions.addPost(newPost);

      setInputValue("");
    } else {
      Navigate("/registration");
    }
  };

  return (
    <div>
      <link
        href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"
        rel="stylesheet"
      ></link>
      <div className="container">
        <div className="profile-wrapper">
          <div className="profile-section-main">
            <ul className="nav nav-tabs profile-tabs" role="tablist">
              <li className="nav-item">
                <a
                  className="nav-link active"
                  data-toggle="tab"
                  href="#profile-overview"
                  role="tab"
                >
                  Timeline
                </a>
              </li>
            </ul>

            <div className="tab-content profile-tabs-content">
              <div
                className="tab-pane active"
                id="profile-overview"
                role="tabpanel"
              >
                <div className="post-editor">
                  <textarea
                    onChange={(e) => setInputValue(e.target.value)}
                    value={inputValue}
                    name="post-field"
                    id="post-field"
                    className="post-field"
                    placeholder="Write Something Cool!"
                  ></textarea>
                  <div className="d-flex">
                    <button
                      className="btn btn-success px-4 py-1"
                      onClick={() => onPost()}
                    >
                      Post
                    </button>
                  </div>
                </div>

                <div className="stream-posts">
                  {store.posts.map((post, index) => {
                    return (
                      <div className="stream-post" key={index}>
                        <div className="sp-author">
                          <a href="#" className="sp-author-avatar">
                            <img
                              src="https://bootdey.com/img/Content/avatar/avatar6.png"
                              alt=""
                            ></img>
                          </a>
                          <h6 className="sp-author-name">
                            <a href="#">
                              {post.user.first_name + " " + post.user.last_name}
                            </a>
                          </h6>
                        </div>
                        <div className="sp-content">
                          <div className="sp-info">{post.time_created}</div>
                          <p className="sp-paragraph mb-0">{post.text}</p>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Wall;
