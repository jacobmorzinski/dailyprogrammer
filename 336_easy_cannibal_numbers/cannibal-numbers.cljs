; -*- clojure -*-

; https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

(ns cannibal_numbers.core
    (:require lumo.io))

(defn -main [infile & args]
    (doall
        (println "infile is" infile)
        (print (lumo.io/slurp infile))))

(set! *main-cli-fn* -main)
