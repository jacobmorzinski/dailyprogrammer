open System.Web.Configuration.Internal
// https://www.reddit.com/r/dailyprogrammer/comments/6ze9z0/20170911_challenge_331_easy_the_adding_calculator/
// Doesn't fullfil all the requirements, but it's a start.

printfn "Command line arguments: "

#if COMPILED
let args = System.Environment.GetCommandLineArgs()
#else // INTERACTIVE
let args = fsi.CommandLineArgs
#endif

for arg in args do
  printfn "%s" arg

let add a b = a + b

let rec _sub a b acc =
  match a with
    | a when a = b -> acc
    | _ -> _sub a (b + 1) (acc + 1)

let sub a b = 
  match a with
    | a when a < b -> - _sub b a 0
    | a when a > b -> _sub a b 0
    | _ -> 0

let rec _mul a b acc cnt =
  match cnt with
    | cnt when cnt = b -> acc
    | _ -> _mul a b (acc + a) (cnt + 1)

let mul a b =
  match b with
    | b when b = 0 -> 0
    | _ -> _mul a b 0 0

let rec _div a b acc cnt =
  match a with
    | a when acc > a -> None
    | a when acc = a -> Some(cnt)
    | a when acc < a -> _div a b (acc + b) (cnt + 1)
    | _ -> None

let div a b =
  match b with
    | 0 -> Some(0)
    | _ -> _div a b 0 0

let x = 9
let y = 3

printfn "add %d %d == %d" x y (add x y)
printfn "sub %d %d == %d" x y (sub x y)
printfn "mul %d %d == %d" x y (mul x y)
printfn "div %d %d == %d" x y (match (div x y) with | Some(x) -> x | None -> 0)
