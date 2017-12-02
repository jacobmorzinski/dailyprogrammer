open System

let readlines () =
    fun _ -> Console.ReadLine()
    |> Seq.initInfinite
    |> Seq.takeWhile ((<>) null)


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

let a85encode ( s : string ) =
    let bytes =
        s
        |> Text.Encoding.ASCII.GetBytes
        |> Seq.map int
    bytes
    |> Seq.chunkBySize 4 // make nested seqs
    |> Seq.map fourByteValue
    |> Seq.map factorBy85
    |> Seq.concat // flatten the nested seqs
    |> Seq.map ((+) 33)
    |> Seq.map byte
    |> Seq.toArray
    |> Text.Encoding.ASCII.GetString

let multiply85 ( input: int[] ) =
    match input with
        | [| a; b; c; d; e |] -> ((((a*85 + b)*85) + c)*85 + d)*85 + e
        | [| a; b; c; d; |] -> ((((a*85 + b)*85) + c)*85 + d)*85
        | [| a; b; c; |] -> ((((a*85 + b)*85) + c)*85 )*85
        | [| a; b; |] -> ((((a*85 + b)*85) )*85 )*85
        | [| a; |] -> ((((a*85 )*85) )*85 )*85
        | _ -> failwith "Error decoding a chunk of 5"

let factorBy256 (input: int) = seq<int> {
    let divisors = [ 256; 256; 256; 256 ]
    let result = divisors |> Seq.fold allYourBase ( input, [] )
    match result with
        | (q, results) -> for i in results do yield i
}

let a85decode ( s : string ) =
    let bytes = 
        s
        |> Text.Encoding.ASCII.GetBytes
        |> Seq.map int
    bytes
    |> Seq.map ((+) -33)
    |> Seq.chunkBySize 5 // make nested maps
    |> Seq.map multiply85
    |> Seq.map factorBy256
    |> Seq.concat // flatten the nested seqs
    |> Seq.map byte
    |> Seq.toArray
    |> Text.Encoding.ASCII.GetString

let solve ( s: string ) =
    let ( ed : string [] ) = s.Split([|' '|], 2)
    match ed with
        | [|"e"; p|] -> a85encode p
        // | [|"d"; c|] -> a85decode c
        | _ -> failwith ("Not Valid: " + s)

let main() =
    let lines = readlines()
    // let results =
    //     Seq.map solve lines
    // Seq.iter ( printfn "%A" ) results

    printfn "%A" ( a85decode "87cURD_*#TDfTZ)+TOAZ" )

main()