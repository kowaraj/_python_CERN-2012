(defn memo
  [f]
  (let [cache (atom {})]
    (println "memo-args: " f)
    (defn proxyf [& args]
      (println "proxyf-args: " args)
      (if-let [e (find @cache args)]
	(val e)
	(let [ret (apply f args)]
	  (swap! cache assoc args ret)
	  ret)))))


(defn slow_add [a b]
  (+ a b))

(defn slow_mul [a b]
  (+ a b))


(def fast_add (memo slow_add))
(def fast_mul (memo slow_mul))
