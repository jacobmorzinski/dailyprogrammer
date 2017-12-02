
let fourByteValue ( input : int[] ) =
    match input with
    | [| a; b; c; d |] -> ((a*256 + b)*256 + c)*256 + d
    | [| a; b; c |] -> ((a*256 + b)*256 + c)*256
    | [| a; b |] -> ((a*256 + b)*256 )*256
    | [| a |] -> ((a*256 )*256 )*256
    | _ -> failwith "Error encoding a chunk of 4"

// The quotient of step N becomes the dividend of step N+1,
// and the remainders are accumulated in the result list.
let allYourBase (dividend, results: list<int>) (divisor) =
    let remainder = dividend % divisor
    let quotient = dividend / divisor
    (quotient , remainder :: results)

let factorBy85 ( input: int ) = seq<int> {
    let five85s = seq { for i in 0 .. 4 -> ( 85 ) }
    let result = five85s |> Seq.fold allYourBase ( input, [] )
    match result with
        | (q, results) -> for i in results do yield i
        // | _ -> failwith "Error dividing into 85s"
}

// The answer of step N becomes the input of step N+1
let baseMul (input, result) (multiplier) =
    let answer = input * multiplier + result
    answer

let multBy85 (input: seq<int>) =
    let multiplier = 85
    input
    |> Seq.fold (fun s -> ((+) (s * multiplier))) 0


1214606444
|> factorBy85
|> multBy85
|> printfn "%A"
