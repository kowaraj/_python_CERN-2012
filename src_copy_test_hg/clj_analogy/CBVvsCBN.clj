(declare lloop)
(defn lloop [] (println "in lloop") lloop)
(defn first_arg [x y] x)

(first_arg 2 4/0)
(first_arg 2 lloop)
(first_arg lloop 3)


