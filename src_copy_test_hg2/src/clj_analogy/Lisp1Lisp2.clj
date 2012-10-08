(defn print-sq [list2]
  (println list)
  (println list2)
  (map list list2))

(print-sq '(1 2 3))

(defn print-sq [list]
  (println (type list))
  (map list list))

(print-sq '(1 2 3))
