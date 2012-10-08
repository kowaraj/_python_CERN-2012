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
  (* a b))


(def fast_add (memo slow_add))
(def fast_mul (memo slow_mul))


;;==============================
;; in clojure

(defn add [a b]
  (+ a b))

(def add (memo add))


;;==============================
;; in python

; @memo
; def add(a, b):
;    return a+b
;
; #alternatively:
;
; add = memo(add)
;




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; another decorators...

(defn inc_res_by [inc_k]
  (fn [f]
    (fn [& args]
      (+ (apply f args) inc_k))))

(defn add [x y]
  (+ x y))

(def add_decorated ((inc_res_by 10) add))

;;==============================
;; in python this would be

; @inc_res_by(10)
; def add(a, b):
;    return a+b
;
; #alternatively:
;
; add = inc_res_by(10)(add)



;;(defn inc_res_by
;; [inc_k]
;;  (fn [f]
;;   (println "fn1-args: " f)
;;    (fn [& args]
;;      (println "fn2-args: " args)
;;      (+ (apply f args) inc_k))))
