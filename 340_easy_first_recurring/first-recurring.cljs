; -*- clojure -*-

; https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

(def state (atom {:answer false}))

(defn handle-line [line]
    (doall
        (for [c line]
            (if-not (@state :answer)
                (if-not (@state c) ; have we seen it?
                    (swap! state update c inc) ; we've seen it
                    (swap! state assoc :answer c))))))

; Bug: printing output should be at the end of each line.
(defn done []
    (println "first recurring character:" (:answer @state)))

(defn -main [& args]
    (let [readline (js/require "readline")
        rl (.createInterface readline
        ; To suppress input echo when stdin is a pipe, set :terminal true.
        ; By default the :terminal option would test process.stdout
                            (clj->js {:input js/process.stdin
                                    :output js/process.stdout
                                    :terminal (.-isTTY js/process.stdin)
                                    }))]
        (.on rl "line"
            handle-line)
        (.on rl "close"
            done)))

(set! *main-cli-fn* -main)
